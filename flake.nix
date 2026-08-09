{
  description = "bsfetch - Fetch BS system information";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f system);
    in
    {
      packages = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };

            bsfetchBin = pkgs.writers.writePython3Bin "bsfetch" { 
                flakeIgnore = [ "E501" "E265" ]; 
                libraries = with pkgs.python3Packages; [ colorama ];
            } (
            builtins.readFile ./bsfetch.py
          );
        in
        {
          bsfetch = pkgs.symlinkJoin {
            name = "bsfetch";
            paths = [ bsfetchBin ];
            nativeBuildInputs = [ pkgs.makeWrapper ];
            postBuild = ''
              mkdir -p $out/share/logo
              cp ${./logo}/* $out/share/logo
              wrapProgram $out/bin/bsfetch \
                --set BSFETCH_LOGO_DIR $out/share/logo
            '';
          };
          default = self.packages.${system}.bsfetch;
        }
      );

      overlays.default = final: prev: {
        bsfetch = self.packages.${final.system}.bsfetch;
      };

      nixosModules.default = { config, pkgs, ... }: {
        nixpkgs.overlays = [ self.overlays.default ];
      };

      apps = forAllSystems (system: {
        bsfetch = {
          type = "app";
          program = "${self.packages.${system}.bsfetch}/bin/bsfetch";
        };
        default = self.apps.${system}.bsfetch;
      });

      devShells = forAllSystems (system:
        let
          pkgs = import nixpkgs { inherit system; };
        in
        {
          default = pkgs.mkShell {
            buildInputs = with pkgs; [
              (python314.withPackages (pypkgs: with pypkgs; [
                pillow
                cairosvg
                colorama
              ]))
            cairo
            ];

            LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
                pkgs.stdenv.cc.cc
                pkgs.cairo
            ];

            shellHook = ''
                export BSFETCH_LOGO_DIR=${./logo}
              '';
          };
        }
      );
    };
}