import os
import logging
import unittest
from mypalette import visualize_palette

logger = logging.getLogger(__name__)
os.chdir(os.path.dirname(__file__))

class test_visualize_palette_correct(unittest.TestCase):
    """
    Testing the class visualize_palette attributes
    """
    def setUp(self):
        """ """

    def test_correct(self):
        visualize_palette(json_path = 'data/test_palette.json')
        self.assertTrue(os.path.isfile('data/test_palette.png'))
        os.remove('data/test_palette.png')

    def test_correct_pdf(self):
        visualize_palette(json_path = 'data/test_palette.json', save_type='pdf')
        self.assertTrue(os.path.isfile('data/test_palette.pdf'))
        os.remove('data/test_palette.pdf')

    def test_correct_no_save_file(self):
        visualize_palette(json_path = 'data/test_palette.json', save_plot=False)
        self.assertFalse(os.path.isfile('data/test_palette.png'))

    def test_incorrect_path(self):
        with self.assertRaises(FileNotFoundError):
            visualize_palette(json_path = 'data/xxx.json')
    
    def test_incorrect_boolean(self):
        with self.assertRaises(FileNotFoundError):
            visualize_palette(json_path = 'data/test_palette.png', save_type='xxx')
