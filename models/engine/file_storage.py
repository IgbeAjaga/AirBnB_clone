#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise, do nothing)."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    class_ref = models.classes.get(class_name)
                    obj = class_ref(**value)
                    FileStorage.__objects[key] = obj

    def all(self):
        """Return the dictionary with all objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['__class__'] = class_name
                    obj_dict[key]['created_at'] = datetime.datetime.strptime(obj_dict[key]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict[key]['updated_at'] = datetime.datetime.strptime(obj_dict[key]['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    if class_name == 'User':
                        obj = User(**value)
                    else:
                        obj = eval(class_name)(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass

    def all(self):
        """Return the dictionary with all objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['__class__'] = class_name
                    obj_dict[key]['created_at'] = datetime.datetime.strptime(obj_dict[key]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict[key]['updated_at'] = datetime.datetime.strptime(obj_dict[key]['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    if class_name == 'User':
                        obj = User(**value)
                    elif class_name == 'Place':
                        obj = Place(**value)
                    elif class_name == 'State':
                        obj = State(**value)
                    elif class_name == 'City':
                        obj = City(**value)
                    elif class_name == 'Amenity':
                        obj = Amenity(**value)
                    elif class_name == 'Review':
                        obj = Review(**value)
                    else:
                        obj = eval(class_name)(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
