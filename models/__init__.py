#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage for usage"""
#from models.engine.file_storage import FileStorage
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

#storage = FileStorage()
if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
