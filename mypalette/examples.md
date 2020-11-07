# Examples
## Load Palette
Download palette.txt from https://coolors.co/5fad56-f5e663-410b9b-ef271b-f9c80e
```python
from mypalette import LoadPalette, visualize_palette
palette = LoadPalette()
p = palette.create_new_palette(input_txt='palette.txt', output_json='palette.json')
p
```
It results:
```
{'HEXs': ['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e'],
 'RGBs': [(0.37254901960784315, 0.6784313725490196, 0.33725490196078434),
  (0.9607843137254902, 0.9019607843137255, 0.38823529411764707),
  (0.2549019607843137, 0.043137254901960784, 0.6078431372549019),
  (0.9372549019607843, 0.15294117647058825, 0.10588235294117647),
  (0.9764705882352941, 0.7843137254901961, 0.054901960784313725)],
 'Names': ['Bud Green', 'Corn', 'Trypan Blue', 'Red Pigment', 'Jonquil']}
```

## Create Palette From Hex List
```python
p = LoadPalette()
#from https://coolors.co/5fad56-f5e663-410b9b-ef271b-f9c80e
_ = p.create_palette_from_hex_list(['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e'], output_json='palette_1.json')
#from https://coolors.co/fffffa-515052-000103-333138-ff312e
_ = p.create_palette_from_hex_list(['#fffffa', '#515052', '#000103', '#333138', '#ff312e'], output_json='palette_2.json')
#from https://coolors.co/5bc0eb-acd49c-fde74c-ccd645-9bc53d-c08f39-e55934-f0692b-fa7921-fa8535
_ = p.create_palette_from_hex_list(['#5bc0eb', '#acd49c', '#fde74c', '#ccd645', '#9bc53d', '#c08f39', '#e55934', '#f0692b', '#fa7921', '#fa8535'], output_json='palette_3.json')
```
Same results as for create_new_palette

## Load Palette 
```python
palette.load_palette(json_path='palette.json')
```
```
['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e']
```

## Visualize Palettte 
```python
_ = visualize_palette(json_path = 'palette_1.json')
_ = visualize_palette(json_path = 'palette_2.json')
_ = visualize_palette(json_path = 'palette_3.json')
```
![result](https://github.com/MattiaCinelli/mycolorpalette/blob/master/commons/vs_results.png?raw=true)