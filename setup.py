from setuptools import setup

# Needed for dependencies
INSTALL_REQUIRES = [
      'numpy',
      'pandas',
      'webcolors >=1,<2',
]

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='mypalette',
      version='1.0.0.1',
      url='https://github.com/MattiaCinelli/mycolorpalette',
      description='Define your Python plot style',
      packages=['mypalette'],
      # Needed for dependencies
      # include_package_data=True,
      install_requires=INSTALL_REQUIRES,
      author='Mattia Cinelli',
      author_email='',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
