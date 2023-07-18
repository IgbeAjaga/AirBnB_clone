#!/usr/bin/python3
"""Defines the HBnB console."""
from cmd import Cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(Cmd):

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print("")
        return True

    def emptyline(self):
        pass

    def default(self, arg):
        args = parse(arg)
        action = args[0]
        obj = args[1]
        args = args[2:]

        if action not in self.__class__.__dict__:
            print("*** Unknown syntax: {} {}".format(action, obj))
            return False

        method = getattr(self, action)
        if len(args) > 0:
            return method(obj, *args)
        else:
            return method(obj)

    def do_create(self, arg):
        """Creates a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return False

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return False

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Retrieves a string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return False

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return False

        obj = eval(arg)().get(arg)
        if not obj:
            print("** no instance found **")
            return False

        print(obj.__str__(verbose=True))

    def do_destroy(self, arg):
        """Deletes an instance."""
        if not arg:
            print("** class name missing **")
            return False

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return False

        if not eval(arg)().get(arg):
            print("** no instance found **")
            return False

        eval(arg).remove(arg)
        storage.save()

    def do_all(self, arg):
        """Retrieves a list of string representations of all instances."""
        if arg in self.__classes:
            objs = eval(arg).all()
        else:
            objs = storage.all()

        result = []
        for obj in objs.values():
            result.append(obj.__str__(verbose=True))

        print(result)

    def do_count(self, arg):
        """Retrieves the number of instances of a class."""
        if not arg:
            count = len(storage.all().values())
        else:
            count = len(eval(arg).all())

        print(count)

    def do_update(self, arg):
        """Updates an instance."""
        if not arg:
            print("** class name missing **")
            return False

        if arg not in self.__classes:
            print("** class doesn't exist **")
            return False

        if not arg + "." + arg in storage.all().keys():
            print("** no instance found **")
            return False

        instance = eval(arg)().get(arg + ".{}".format(arg))
        args = arg.split(".")[1:]
        if len(args) == 2:
            key, value = args
            if key in instance.__dict__:
                try:
                    valtype = type(instance.__dict__[key])
                except:
                    valtype = type(eval(value))
                instance.__dict__[key] = valtype
