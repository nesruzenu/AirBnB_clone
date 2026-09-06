#!/usr/bin/python3
"""
Unittests for the FileStorage class.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all(self):
        """Test that all returns the __objects dictionary."""
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        """Test that new adds an object to __objects."""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        key = "{}.{}".format(bm.__class__.__name__, bm.id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
