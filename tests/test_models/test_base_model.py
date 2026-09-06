#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init_no_args(self):
        """Test instantiation with no arguments."""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_str_representation(self):
        """Test the __str__ method output format."""
        bm = BaseModel()
        expected = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates updated_at."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        sleep(0.01)
        bm.save()
        self.assertNotEqual(old_updated_at, bm.updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains expected keys."""
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIn("id", d)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)
        self.assertIn("__class__", d)

    def test_to_dict_datetime_is_str(self):
        """Test that created_at/updated_at are strings in to_dict()."""
        bm = BaseModel()
        d = bm.to_dict()
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_init_from_dict(self):
        """Test creating a new instance from a dictionary."""
        bm = BaseModel()
        bm.name = "Test"
        bm_dict = bm.to_dict()
        new_bm = BaseModel(**bm_dict)
        self.assertEqual(bm.id, new_bm.id)
        self.assertEqual(bm.created_at, new_bm.created_at)
        self.assertEqual(bm.updated_at, new_bm.updated_at)
        self.assertEqual(bm.name, new_bm.name)
        self.assertIsNot(bm, new_bm)


if __name__ == "__main__":
    unittest.main()
