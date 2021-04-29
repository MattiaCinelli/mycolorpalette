from mypalette.src.load_palette import LoadPalette
from mypalette.src.visualize_palette import visualize_palette

palette = LoadPalette()
p = palette.create_palette_from_hex_list(
    ["#5fad56", "#f5e663", "#410b9b", "#ef271b", "#f9c80e"],
    output_json="palette.json",
)

visualize_palette(json_path = 'palette.json')