#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
from os.path import exists
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_general(self):
        f1 = FileStorage()
        f1.all().clear()
        f1.reload()
        self.assertTrue(len(f1.all()) != 0)
