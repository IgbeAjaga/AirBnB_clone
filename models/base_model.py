#!/usr/bin/python3
"""Defines the class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
    """Initialize a new BaseModel.
    Args:
    *args (any): Unused.
    **kwargs (dict): Key pairs of attributes.
    """
    if kwargs:
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                else:
                    models.storage.new(self)

    def __str__(self):
        """Return the str reps of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updating with current time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
    	obj_dict = self.__dict__.copy()
    	obj_dict['__class__'] = self.__class__.__name__
    	obj_dict['created_at'] = self.created_at.isoformat()
    	obj_dict['updated_at'] = self.updated_at.isoformat()
    	return obj_dict
