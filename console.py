#!/usr/bin/python3
"""Console module."""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The HBNB console functionalities."""
    prompt = '(hbnb)'
    intro = ""
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, command):
        """ Method to exit the HBNB console."""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit."""
        print("Quit to exit the program\n")

    def do_EOF(self, arg):
        """Handles EOF to exit program."""
        print()
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF."""
        print("Exits the program without formatting\n")

    def emptyline(self):
        """Overrides the CMD emptline method."""
        pass

    def do_create(self, args):
        """Creates an object of any class."""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        print(new_instance.id)

    def help_create(self):
        """Help information for create command."""
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """Method that show an inividual object."""
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """Help information for show command."""
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """Destroys a specified object. """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            del(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for destroy command."""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        """Shows all objects of a class/ all objects. """
        print_list = []

        if args:
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """Help information for all command."""
        print("Shows all objects, or all instances of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """Updates a cetain onbejct with new information. """
        new = args.split(" ")
        try:
            c_name = new[0]
            c_id = new[2]
            key = c_name + "." + c_id
            attr_name = new[3]
            attr_value = new[4]
        except Exception:
            pass

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return
        if key not in storage._FileStorage__objects:
            print("** no instance found **")
            return

        if not attr_name:
            print("** attribute name missing **")
            return

        if not attr_value:
            print("** value missing **")
            return

        try:
            new_dict = storge._FileStorage__objects[key]
            new_dict.update({attr_name: attr_val})
        except KeyError:
            print("** no instance found **")

    def help_update(self):
        """Help information for the update class."""
        print("Updates an object woth new information")
        print("Usage: update <className> <id> <attName> <attValue>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
