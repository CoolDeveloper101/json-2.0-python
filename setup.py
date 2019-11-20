from setuptools import setup


setup(
  name = 'json2',
  version = '0.1.0',
  description = 'This is a wrapper around the json module, which uses pickle to store a wide variety of objects.',
  long_description = '''This is a wrapper around the json module, which uses pickle to store a wide variety of objects.
Json is a nice format, but it does not let you store a custom data type. This module lets you store custom objects, which can be used in a wide variety of tasks. For example, you cannot store a numpy array using json but using this module, you can. Currently, it can only store dictionaries.''',
  author = 'CoolDeveloper101',
  url = 'https://github.com/CoolDeveloper101/json-2.0-python/',
  packages = ['json2'],
)
