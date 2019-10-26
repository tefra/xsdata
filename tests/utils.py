import unittest
from os import path

fixtures_dir = path.join(path.dirname(path.abspath(__file__)), "xsd")


class ModelTestCase(unittest.TestCase):
    @staticmethod
    def fixture_path(file_name):
        return "{}/{}.xsd".format(fixtures_dir, file_name)
