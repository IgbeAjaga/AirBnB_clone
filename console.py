#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
	"""Command interpreter class."""

	prompt = "(hbnb) "

	def do_quit(self, arg):
    	"""Quit command to exit the program."""
    	return True

	def do_EOF(self, arg):
    	"""EOF command to exit the program."""
    	return True

	def emptyline(self):
    	"""Handles empty line input."""
    	pass

	def do_create(self, arg):
    	"""Creates a new instance of a class and saves it to the JSON file."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	else:
        	new_obj = eval(args[0])()
        	new_obj.save()
        	print(new_obj.id)

	def do_show(self, arg):
    	"""Prints the string representation of an instance."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	elif len(args) == 1:
        	print("** instance id missing **")
    	else:
        	obj_key = f"{args[0]}.{args[1]}"
        	if obj_key in storage.all():
            	obj = storage.all()[obj_key]
            	print(obj)
        	else:
            	print("** no instance found **")

	def do_destroy(self, arg):
    	"""Deletes an instance based on the class name and id."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	elif len(args) == 1:
        	print("** instance id missing **")
    	else:
        	obj_key = f"{args[0]}.{args[1]}"
        	if obj_key in storage.all():
            	del storage.all()[obj_key]
            	storage.save()
        	else:
            	print("** no instance found **")

	def do_all(self, arg):
    	"""Prints all string representations of instances or instances of a specific class."""
    	args = arg.split()
    	if len(args) == 0 or args[0] in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	if len(args) > 0:
            	class_name = args[0]
            	if class_name in globals():
                	class_obj = globals()[class_name]
                	instance_list = class_obj.all()
                	print([str(instance) for instance in instance_list])
                	return
            	else:
                	print("** class doesn't exist **")
                	return
        	obj_list = []
        	for obj_key in storage.all():
            	if len(args) == 0 or args[0] == storage.all()[obj_key].__class__.__name__:
                	obj_list.append(str(storage.all()[obj_key]))
        	print(obj_list)
    	else:
        	print("** class doesn't exist **")

	def do_count(self, arg):
    	"""Prints the number of instances of a class."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	else:
        	class_name = args[0]
        	if class_name in globals():
            	class_obj = globals()[class_name]
            	instance_count = len(class_obj.all())
            	print(instance_count)
        	else:
            	print("** class doesn't exist **")

	def do_update(self, arg):
    	"""Updates an instance based on the class name and id."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	elif len(args) == 1:
        	print("** instance id missing **")
    	elif f"{args[0]}.{args[1]}" not in storage.all():
        	print("** no instance found **")
    	elif len(args) == 2:
        	print("** attribute name missing **")
    	elif len(args) == 3:
        	print("** value missing **")
    	else:
        	obj_key = f"{args[0]}.{args[1]}"
        	obj = storage.all().get(obj_key)
        	if obj:
            	if not isinstance(eval(args[2]), dict):
                	print("** value must be a dictionary **")
                	return
            	attr_dict = eval(args[2])
            	for attr_name, attr_value in attr_dict.items():
                	setattr(obj, attr_name, attr_value)
            	obj.save()
        	else:
            	print("** no instance found **")

	def do_classmethod(self, arg):
    	"""Classmethod command to execute a class method."""
    	args = arg.split()
    	if len(args) == 0:
        	print("** class name missing **")
    	elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
        	print("** class doesn't exist **")
    	elif len(args) == 1:
        	print("** method name missing **")
    	else:
        	class_name = args[0]
        	method_name = args[1]
        	if class_name in globals():
            	class_obj = globals()[class_name]
            	if hasattr(class_obj, method_name):
                	class_method = getattr(class_obj, method_name)
                	class_method()
            	else:
                	print("** method doesn't exist **")
        	else:
            	print("** class doesn't exist **")

	def default(self, line):
    	"""Default command to handle class.method() syntax."""
    	args = line.split(".")
    	if len(args) == 2:
        	class_name = args[0]
        	method_name = args[1]
        	if class_name in globals():
            	class_obj = globals()[class_name]
            	if hasattr(class_obj, method_name):
                	class_method = getattr(class_obj, method_name)
                	class_method()
                	return
    	print("*** Unknown syntax: {}".format(line))

	def do_User(self, arg):
    	"""User command to handle User.<command> syntax."""
    	self.default("User." + arg)

	def do_State(self, arg):
    	"""State command to handle State.<command> syntax."""
    	self.default("State." + arg)

	def do_City(self, arg):
    	"""City command to handle City.<command> syntax."""
    	self.default("City." + arg)

	def do_Amenity(self, arg):
    	"""Amenity command to handle Amenity.<command> syntax."""
    	self.default("Amenity." + arg)

	def do_Place(self, arg):
    	"""Place command to handle Place.<command> syntax."""
    	self.default("Place." + arg)

	def do_Review(self, arg):
    	"""Review command to handle Review.<command> syntax."""
    	self.default("Review." + arg)


if __name__ == "__main__":
	HBNBCommand().cmdloop()
