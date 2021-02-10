import os
import shutil
import tempfile
import logging
import unittest
from mypalette import LoadPalette

logger = logging.getLogger(__name__)
os.chdir(os.path.dirname(__file__))

class test_load_palette_class(unittest.TestCase):
    """
    Testing the class load_palette attributes
    """
    def setUp(self):
        """
        Declearing the object class and the temporal folder
        """
        self.palette = LoadPalette()

    def test_attributes(self):
        """ 
        Test attributes present in the class
        """
        self.assertEqual(len(self.palette.primary), 3)
        self.assertEqual(len(self.palette.secondary), 3)
        self.assertEqual(len(self.palette.tertiary), 6)
        self.assertEqual(len(self.palette.black_white), 2)


class Test_create_new_palette(unittest.TestCase):
    """
    Testing the function create_new_palette
    """
    def setUp(self):
        """
        Declearing the object class and the temporal folder
        """
        self.palette = LoadPalette()
        self.test_dir = tempfile.mkdtemp()
        self.json_file =  os.path.join(self.test_dir, 'test_new_palette.json')

    def tearDown(self):
        """
        Removing temporal folder and its content.
        """
        shutil.rmtree(self.test_dir)

    def test_correct_behaviour(self):
        """
        Test if the method runs correctly and save the file.
        """
        self.p = self.palette.create_new_palette(
            input_txt = 'data/test_palette.txt',
            output_json = self.json_file
            )
        self.assertTrue(os.path.isfile(self.json_file))

    def test_result(self):
        """ 
        Test if the result from create_new_palette is correct
        """
        self.p = self.palette.create_new_palette(
            input_txt = 'data/test_palette.txt',
            output_json = self.json_file
            )
        self.assertIs(type(self.p), dict)
        self.assertIn('HEXs', self.p.keys())
        self.assertIn('RGBs', self.p.keys())
        self.assertIn('Names', self.p.keys())
        self.assertEqual(len(self.p.keys()), 3)
        self.assertEqual(len(self.p['HEXs']), 5)

    def test_missing_value(self):
        """ 
        Test missing values
        """
        with self.assertRaises(TypeError):
            self.palette.create_new_palette()
        with self.assertRaises(TypeError):
            self.palette.create_new_palette(input_txt = 'data/test_palette.txt')
        with self.assertRaises(TypeError):
            self.palette.create_new_palette(output_json = self.json_file)

    def test_missing_files(self):
        """ 
        Test missing file
        """
        with self.assertRaises(FileNotFoundError):
            self.palette.create_new_palette(input_txt = 'data/test_palette2.txt', 
            output_json = self.json_file)


class Test_load_palette_method(unittest.TestCase):
    """
    Testing the function create_new_palette
    """
    def setUp(self):
        """
        Declearing the object class
        """     
        self.palette = LoadPalette()

    def test_load_palette_result_hex(self):
        """
        Testing correct behavior.  
        """
        self.p = self.palette.load_palette(
            json_path = 'data/test_palette.json')

        self.assertIs(type(self.p), list)
        self.assertIs(type(self.p[0]), str)
        self.assertEqual(len(self.p), 5)

    def test_load_palette_result_rgb(self):
        self.p = self.palette.load_palette(
            json_path = 'data/test_palette.json', code = 'RGBs')
        self.assertIs(type(self.p), list)
        self.assertIs(type(self.p[0]), tuple)
        self.assertEqual(len(self.p), 5)

    def test_load_palette_result_names(self):
        self.p = self.palette.load_palette(
            json_path = 'data/test_palette.json', code = 'Names')
        self.assertIs(type(self.p), list)
        self.assertIs(type(self.p[0]), str)
        self.assertEqual(len(self.p), 5)

    def test_load_palette_result_all(self):
        self.p = self.palette.load_palette(
            json_path = 'data/test_palette.json', code = 'All')
        self.assertIs(type(self.p), dict)
        self.assertEqual(len(self.p.keys()), 3)
        self.assertEqual(len(self.p['HEXs']), 5)
    
    def test_load_palette_wrong_code(self):
        with self.assertRaises(KeyError):
            self.palette.load_palette(
                json_path = 'data/test_palette.json', 
                code = 'xxx')

    def test_missing_files(self):
        self.palette = LoadPalette()
        with self.assertRaises(TypeError):
            self.palette.load_palette()

    def test_wrong_entry(self):
        self.palette = LoadPalette()
        with self.assertRaises(FileNotFoundError):
            self.palette.load_palette(json_path='data/test_xxx.json')


class Test_create_palette_from_hex_list(unittest.TestCase):
    """
    Testing the function create_palette_from_hex_list
    """
    def setUp(self):
        """
        Declearing the object class and the temporal folder
        """
        self.palette = LoadPalette()
        self.test_dir = tempfile.mkdtemp()
        self.json_file =  os.path.join(self.test_dir, 'test_new_palette.json')

    def tearDown(self):
        """
        Removing temporal folder and its content.
        """
        shutil.rmtree(self.test_dir)

    def test_missing_hexadecimal(self):
        """ """
        with self.assertRaises(TypeError):
            self.palette.create_palette_from_hex_list()
            
    def test_correct_behaviour(self):
        self.p = self.palette.create_palette_from_hex_list(
            hexadecimal = ['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e'],
            output_json = self.json_file)

        self.assertIs(type(self.p), dict)
        self.assertEqual(len(self.p.keys()), 3)
        
        self.assertEqual(len(self.p['HEXs']), 5)
        self.assertIs(type(self.p['HEXs']), list)
        self.assertIs(type(self.p['HEXs'][0]), str)

        self.assertEqual(len(self.p['RGBs']), 5)
        self.assertIs(type(self.p['RGBs']), list)
        self.assertIs(type(self.p['RGBs'][0]), tuple)

        self.assertEqual(len(self.p['Names']), 5)
        self.assertIs(type(self.p['Names']), list)
        self.assertIs(type(self.p['Names'][0]), str)

    def test_file_exist(self):
        self.p = self.palette.create_palette_from_hex_list(
            hexadecimal = ['#5fad56', '#f5e663', '#410b9b', '#ef271b', '#f9c80e'],
            output_json = self.json_file)
        self.assertTrue(os.path.isfile(self.json_file))


if __name__ == '__main__':
    unittest.main()