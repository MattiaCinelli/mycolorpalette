import os
import pytest
from mypalette import LoadPalette


def test_load_palette_class():
    """
    Testing the class load_palette attributes
    """
    palette = LoadPalette()
    assert len(palette.primary) == 3
    assert len(palette.secondary) == 3
    assert len(palette.tertiary) == 6
    assert len(palette.black_white) == 2
   

# @pytest.fixture(name='palette', scope='class')
def invoke_class():
    a = os.path.join( 'data', 'test_palette.txt')
    b = os.path.join( 'data', 'test_palette.json')
    palette = LoadPalette().create_new_palette(
        input_txt = a,
        output_json = b
        )

def test_correct_behavior():
    """
    Test if the method runs correctly and save the file.
    """
    aaa = os.path.join(os.getcwd(), 'tests', 'data', 'test_palette.json')
    assert os.path.isfile(aaa)==True
    # assert os.path.isfile('data/test_palette.json')
