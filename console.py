#!/usr/bin/env python3
"""
Module for the entry point of the command interpreter
"""
import cmd
import sys
import models
import shlex
from shlex import split
from models import storage
from models.base_model import BaseModel
rom models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing if an empty line is entered
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program at EOF (Ctrl+D)
        """
        print()
        return True

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id.
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = shlex.split(args)
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = shlex.split(args)
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = shlex.split(args)
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all <class name> or all
        """
        arg_list = shlex.split(args)
        objects = storage.all()

        if not arg_list:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = arg_list[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in objects.items() if key.split('.')[0] == class_name])

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not args:
            print("** class name missing **")
            return

        arg_list = shlex.split(args)
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_name = arg_list[2]
        attribute_value = arg_list[3]

        # Check if the attribute exists in the class
        if not hasattr(objects[key], attribute_name):
            print("** attribute doesn't exist **")
            return

        # Convert the attribute value to the appropriate type
        attribute_type = type(getattr(objects[key], attribute_name))
        try:
            attribute_value = attribute_type(attribute_value)
        except ValueError:
            print("** invalid attribute value **")
            return

        setattr(objects[key], attribute_name, attribute_value)
        objects[key].save()

    def do_create(self, arg):
    """Create a new instance of BaseModel, save it to the JSON file and print the id."""
    if not arg:
        print("** class name missing **")
        return
    try:
        cls = eval(arg)
        instance = cls()
        instance.save()
        print(instance.id)
    except NameError:
        print("** class doesn't exist **")

    def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and id."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
    else:
        print(objects[key])

    def do_destroy(self, arg):
    """Deletes an instance based on the class name and id, save the change into the JSON file."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
    else:
        objects.pop(key)
        models.storage.save()

    def do_all(self, arg):
    """Prints all string representation of all instances based or not on the class name."""
    objects = models.storage.all()
    if not arg:
        print([str(obj) for obj in objects.values()])
    else:
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
    """Updates an instance based on the class name and id by adding or updating attribute."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    obj = objects[key]
    attr_name = args[2]
    try:
        value = eval(args[3])
    except NameError:
        value = args[3]
    setattr(obj, attr_name, value)
    models.storage.save()

    def do_create(self, arg):
    """Create a new instance of a class, save it to the JSON file, and print the id."""
    if not arg:
        print("** class name missing **")
        return
    try:
        cls = eval(arg)
        instance = cls()
        instance.save()
        print(instance.id)
    except NameError:
        print("** class doesn't exist **")

    def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and id."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
    else:
        print(objects[key])

    def do_destroy(self, arg):
    """Deletes an instance based on the class name and id, save the change into the JSON file."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
    else:
        objects.pop(key)
        models.storage.save()

    def do_all(self, arg):
    """Prints all string representation of all instances based or not on the class name."""
    objects = models.storage.all()
    if not arg:
        print([str(obj) for obj in objects.values()])
    else:
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
    """Updates an instance based on the class name and id by adding or updating an attribute."""
    if not arg:
        print("** class name missing **")
        return
    args = arg.split()
    if args[0] not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    key = f"{args[0]}.{args[1]}"
    objects = models.storage.all()
    if key not in objects:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    if len(args) < 4:
        print("** value missing **")
        return
    obj = objects[key]
    attr_name = args[2]
    try:
        value = eval(args[3])
    except NameError:
        value = args[3]
    setattr(obj, attr_name, value)
    models.storage.save()

    def do_all(self, arg):
    """Prints all string representation of all instances based or not on the class name."""
    objects = models.storage.all()
    if not arg:
        print([str(obj) for obj in objects.values()])
    else:
        args = arg.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in objects.values() if obj.__class__.__name__ == class_name])

    def do_count(self, arg):
    """Retrieve the number of instances of a class."""
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    objects = models.storage.all()
    count = sum(1 for obj in objects.values() if obj.__class__.__name__ == class_name)
    print(count)

    def do_show(self, arg):
    """Retrieve an instance based on ID."""
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    instance_id = args[1]
    objects = models.storage.all()
    key = "{}.{}".format(class_name, instance_id)
    instance = objects.get(key, None)
    if instance is None:
        print("** no instance found **")
    else:
        print(instance)

    def do_destroy(self, arg):
    """Delete an instance based on ID."""
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    instance_id = args[1]
    objects = models.storage.all()
    key = "{}.{}".format(class_name, instance_id)
    instance = objects.get(key, None)
    if instance is None:
        print("** no instance found **")
    else:
        del objects[key]
        models.storage.save()

    def do_update(self, arg):
    """Update an instance based on ID."""
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    instance_id = args[1]
    objects = models.storage.all()
    key = "{}.{}".format(class_name, instance_id)
    instance = objects.get(key, None)
    if instance is None:
        print("** no instance found **")
        return

    if len(args) < 3:
        print("** attribute name missing **")
        return

    attr_name = args[2]
    if len(args) < 4:
        print("** value missing **")
        return

    attr_value = args[3]
    # Convert the value to the appropriate type if needed (e.g., int, float)
    try:
        attr_value = eval(attr_value)
    except:
        pass

    # Update the attribute
    setattr(instance, attr_name, attr_value)
    instance.updated_at = datetime.now()
    models.storage.save() 

    def do_update(self, arg):
    """Update an instance based on ID with dictionary representation."""
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    instance_id = args[1]
    objects = models.storage.all()
    key = "{}.{}".format(class_name, instance_id)
    instance = objects.get(key, None)
    if instance is None:
        print("** no instance found **")
        return

    if len(args) < 3:
        print("** dictionary missing **")
        return

    try:
        dictionary = eval(" ".join(args[2:]))
        if not isinstance(dictionary, dict):
            raise ValueError()
    except:
        print("** invalid dictionary **")
        return

    for key, value in dictionary.items():
        if hasattr(instance, key):
            setattr(instance, key, value)
    instance.updated_at = datetime.now()
    models.storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
