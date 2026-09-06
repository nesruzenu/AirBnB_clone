#!/usr/bin/python3
"""Defines the BaseModel class."""
import uuid
from datetime import datetime


class BaseModel:
    """Base class that defines all common attributes/methods
    for other classes.
    """

    def __init__(self):
        """Initialize a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__
        of the instance, with created_at and updated_at converted to
        ISO format strings, and __class__ added.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
