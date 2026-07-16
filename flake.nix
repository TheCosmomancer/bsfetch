{
    description = "bsfetch python flake";
    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    };

    outputs =
        { self, nixpkgs, ... }:
        let
            system = "x86_64-linux";
            pkgs = import nixpkgs {
                system = "${system}";
            };
        in
        {
            devShells.${system}.default = pkgs.mkShell {

            buildInputs = with pkgs; [
            
                (python314.withPackages (pypkgs: with pypkgs; [
                    pillow
                    cairosvg
                ]))    
            ];

            LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

            };
        };
}