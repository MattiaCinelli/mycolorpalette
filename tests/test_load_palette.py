import os
import pytest
from mypalette import LoadPalette


@pytest.fixture(scope='session')
def palette():
    '''Returns a LoadPalette instance'''
    return LoadPalette()


def test_load_palette_class(palette):
    """
    Testing the class load_palette attributes
    """
    assert len(palette.primary) == 3
    assert len(palette.secondary) == 3
    assert len(palette.tertiary) == 6
    assert len(palette.black_white) == 2
   

@pytest.mark.parametrize('txt, JSON', [
   (os.path.join(os.getcwd(), 'tests', 'data', 'test_palette.txt'),
    os.path.join(os.getcwd(), 'tests', 'data', 'test_palette.JSON'))
])
def test_create_new_palette(palette, txt, JSON):
    p = palette.create_new_palette(
        input_txt = txt,
        output_json = JSON
        )
    assert type(p) == dict
    assert len(p) == 3
    assert list(p.keys()) == ['HEXs', 'RGBs', 'Names']
    assert len(p['HEXs']) == 5
    assert len(p['RGBs']) == 5
    assert len(p['Names']) == 5


@pytest.mark.parametrize('JSON', [
   (os.path.join(os.getcwd(), 'tests', 'data', 'test_palette.JSON'))
])
def test_correct_behavior(JSON):
    """
    If create_new_palette runs correctly it will save a JSON file.
    """
    assert os.path.isfile(JSON)==True