#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
	"""File storage class for serialization and deserialization of objects."""

	__file_path = "file.json"
	__objects = {}

	def all(self):
    	"""Returns the dictionary __objects."""
    	return self.__objects

	def new(self, obj):
    	"""Sets in __objects the obj with key <obj class name>.id."""
    	key = f"{obj.__class__.__name__}.{obj.id}"
    	self.__objects[key] = obj

	def save(self):
    	"""Serializes __objects to the JSON file (path: __file_path)."""
    	new_dict = {}
    	for key, value in self.__objects.items():
        	new_dict[key] = value.to_dict()
    	with open(self.__file_path, "w") as file:
        	json.dump(new_dict, file)

	def reload(self):
    	"""Deserializes the JSON file to __objects."""
    	try:
        	with open(self.__file_path, "r") as file:
            	obj_dict = json.load(file)
            	for key, value in obj_dict.items():
                	cls_name, obj_id = key.split(".")
                	class_map = {
                    	"BaseModel": BaseModel,
                    	"User": User,
                    	"State": State,
                    	"City": City,
                    	"Amenity": Amenity,
                    	"Place": Place,
                    	"Review": Review
                	}
                	cls = class_map[cls_name]
                	self.__objects[key] = cls(**value)
    	except FileNotFoundError:
        	pass
