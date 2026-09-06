#!/usr/bin/python3
"""
Initialize the models package and set up FileStorage.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
