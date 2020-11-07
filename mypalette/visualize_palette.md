# Visualize Palettte 
```python
from mypalette import LoadPalette, visualize_palette
p = LoadPalette()
#from https://coolors.co/5fad56-f5e663-410b9b-ef271b-f9c80e
_ = p.create_palette_from_hex_list(['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e'], output_json='palette_1.json')
#from https://coolors.co/fffffa-515052-000103-333138-ff312e
_ = p.create_palette_from_hex_list(['#fffffa', '#515052', '#000103', '#333138', '#ff312e'], output_json='palette_2.json')
#from https://coolors.co/5bc0eb-acd49c-fde74c-ccd645-9bc53d-c08f39-e55934-f0692b-fa7921-fa8535
_ = p.create_palette_from_hex_list(['#5bc0eb', '#acd49c', '#fde74c', '#ccd645', '#9bc53d', '#c08f39', '#e55934', '#f0692b', '#fa7921', '#fa8535'], output_json='palette_3.json')
```

```python
_ = visualize_palette(json_path = 'palette_1.json')
_ = visualize_palette(json_path = 'palette_2.json')
_ = visualize_palette(json_path = 'palette_3.json')
```
![result](https://github.com/MattiaCinelli/mycolorpalette/blob/master/commons/vs_results.png?raw=true)
