def main():

    from pathlib import Path
    from PIL import Image
    from cairosvg import svg2png

    SCRIPT_DIR = Path(__file__).resolve().parent
    INPUT_DIR = SCRIPT_DIR / "unrefined_logo"
    OUTPUT_DIR = SCRIPT_DIR / "logo"

    files = [f for f in INPUT_DIR.iterdir() if f.is_file()]

    converted_count = 0

    for file_path in files:
        ext = file_path.suffix.lower()
        formatted_name = file_path.stem
        output_path = OUTPUT_DIR / f"{formatted_name}.png"

        try:
            if ext == '.svg':
                svg2png(
                    url=str(file_path), write_to=str(output_path)
                    ,output_height=512
                    )
                print(f"  [SVG -> PNG] {file_path.name} -> {output_path.name}")

            elif ext == '.png':
                with Image.open(file_path) as img:
                    img = img.convert('RGBA')
                    img.save(output_path, format='PNG')
                print(f"  [PNG -> PNG] {file_path.name} -> {output_path.name}")

            else:
                with Image.open(file_path) as img:
                    img = img.convert('RGBA')
                    img.save(output_path, format='PNG')
                print(f"  [{ext.upper()[1:]} -> PNG] {file_path.name} -> {output_path.name}")

            converted_count += 1

        except Exception as e:
            print(f"  [ERROR] Failed to convert {file_path.name}: {e}")

    print(f"\nDone! Converted {converted_count}/{len(files)} logos from {INPUT_DIR} into '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    main()