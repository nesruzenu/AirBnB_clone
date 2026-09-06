#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment before each test."""
        self.file_path = FileStorage._FileStorage__file_path
        # Preserve any existing objects/file so tests don't clobber them
        self._backup_objects = FileStorage._FileStorage__objects.copy()
        FileStorage._FileStorage__objects.clear()
        if os.path.exists(self.file_path):
            os.rename(self.file_path, self.file_path + ".bak")

    def tearDown(self):
        """Clean up test environment after each test."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.file_path + ".bak"):
            os.rename(self.file_path + ".bak", self.file_path)
        FileStorage._FileStorage__objects.clear()
        FileStorage._FileStorage__objects.update(self._backup_objects)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_no_args(self):
        """Test that all() with no arguments returns __objects."""
        result = storage.all()
        self.assertIs(result, FileStorage._FileStorage__objects)

    def test_new_adds_object(self):
        """Test that new() adds an object to __objects."""
        bm = BaseModel()
        key = "BaseModel." + bm.id
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key], bm)

    def test_new_sets_correct_key_format(self):
        """Test the key format used by new()."""
        bm = BaseModel()
        expected_key = "{}.{}".format(type(bm).__name__, bm.id)
        self.assertIn(expected_key, storage.all().keys())

    def test_save_creates_file(self):
        """Test that save() creates the JSON file."""
        BaseModel()
        storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_save_file_content(self):
        """Test that save() writes correct JSON content."""
        bm = BaseModel()
        storage.save()
        with open(self.file_path, "r") as f:
            content = json.load(f)
        key = "BaseModel." + bm.id
        self.assertIn(key, content)
        self.assertEqual(content[key]["id"], bm.id)

    def test_reload_no_file(self):
        """Test that reload() does nothing if the file doesn't exist."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload() raised an exception: {}".format(e))

    def test_reload_restores_objects(self):
        """Test that reload() correctly restores objects from file."""
        bm = BaseModel()
        bm.name = "Test_Reload"
        bm_id = bm.id
        storage.save()

        # Clear in-memory objects to simulate a fresh start
        FileStorage._FileStorage__objects.clear()
        storage.reload()

        key = "BaseModel." + bm_id
        self.assertIn(key, storage.all())
        reloaded_obj = storage.all()[key]
        self.assertEqual(reloaded_obj.id, bm_id)
        self.assertEqual(reloaded_obj.name, "Test_Reload")

    def test_reload_preserves_datetime_types(self):
        """Test that reload() converts dates back to datetime objects."""
        from datetime import datetime
        bm = BaseModel()
        storage.save()
        FileStorage._FileStorage__objects.clear()
        storage.reload()

        key = "BaseModel." + bm.id
        reloaded_obj = storage.all()[key]
        self.assertIsInstance(reloaded_obj.created_at, datetime)
        self.assertIsInstance(reloaded_obj.updated_at, datetime)

    def test_file_path_is_private_class_attr(self):
        """Test that __file_path is a private class attribute."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_objects_is_private_class_attr(self):
        """Test that __objects is a private class attribute."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))


if __name__ == "__main__":
    unittest.main()
