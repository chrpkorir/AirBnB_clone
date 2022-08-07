#!/usr/bin/python3
"""Console module."""

import cmd
from inspect import Arguments
import re
from pprint import pprint
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """The HBNB console functionalities."""
    prompt = '(hbnb)'
    intro = ""

    def parseline(self, line):

        if '.' in line and '(' in line and ')' in line:
            toks = re.split(r'\.|\(|\)', line)
            toks[2] = toks[2].strip('"').replace(',', ' ')
            newline = toks[1] + ' ' + toks[0] + ' ' + toks[2]
            if toks[2] == '':
                line = (toks[1], toks[0], newline)
            else:
                line = (toks[1], toks[0] + " " + toks[2], newline)

            if toks[1] == 'count':
                self.count(toks[0])
                return cmd.Cmd.parseline(self, '')
            return line
        return cmd.Cmd.parseline(self, line)

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

    def count(self, args):
        """counts the number of instance of class"""
        if args == "all":
            for arg in storage.classes():
                self.countone(arg)
        else:
            self.countone(args)

    def countone(self, args):
        """counts the number of instance of class"""
        n = 0
        for k, v in storage.all().items():
            if type(v).__name__ == args:
                n += 1
        print(f"{n} Intances of {args}")
        print(n)

    def help_count(self):
        print("**counts the instances of a class")

    def do_create(self, args):
        """Creates an object of any class."""
        if not args:
            print("** class name missing **")
            return
        elif args not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[args]()
        new_instance.save()
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

        if c_name not in storage.classes():
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
        if c_id == "all":
            for k, v in list(storage.all().items()):
                idclass = k.split('.')
                if idclass[0] == c_name:
                    self.delete_instance(idclass[0], idclass[1])

        else:
            self.delete_instance(c_name, c_id)

        storage.save()

    def delete_instance(self, name, id):
        """helper function for destroying an object instance"""
        if not name:
            print("** class name missing **")
            return

        if name not in storage.classes():
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return

        key = name + "." + id
        try:
            del storage.all()[key]

        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """Help information for destroy command."""
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        print_list = []
        if args:
            if args not in storage.classes():
                print("** class doesn't exist **")
                return
            for k, v in storage._FileStorage__objects.items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage._FileStorage__objects.items():
                print_list.append(str(v))

        pprint(print_list, indent=1)

    def help_all(self):
        """Help information for all command."""
        print("Shows all objects, or all instances of a class")
        print("[Usage]: all <className>\n")

    def do_update(self, args):
        """Updates a cetain onbejct with new information. """
        print("========= update args ============")
        print(args)
        new = args.split(" ")
        print("=== new =====")
        print(new)
        for word in range(len(new)):
            new[word] = self.strip_quotes(new[word])

        del new[2]
        del new[3]
        print("=== stripped words =====")
        print(new)

        if len(new) < 4:
            print("new value missing")
            return
        if len(new) < 3:
            print("attibute name missing")
            return
        try:
            c_name = new[0]
            c_id = new[1]
            key = c_name + "." + c_id
            attr_name = new[2]
            attr_value = new[3]

        except Exception:
            pass

        print("=== update args, name , id , attr name, attr value =====")
        print(c_name, c_id, self.strip_quotes(
            new[2]), self.strip_quotes(new[3]))

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in storage.classes():
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

            new_dict = storage.all()[key].to_dict()
            print(new_dict)
            new_dict[attr_name] = attr_value
            storage.update(new_dict, key)
            # new_dict.update({attr_name: attr_value})
            # storage.save()
        except KeyError:
            print("** no instance found **")

    def help_update(self):
        """Help information for the update class."""
        print("Updates an object woth new information")
        print("Usage: update <className> <id> <attName> <attValue>\n")
        print("Usage: update <className> <id> <attName> <attValue>\n")

    def strip_quotes(self, str):
        if not str:
            return
        if str[0] == '"' and str[len(str) - 1] == '"':
            return str[1:len(str) - 1]
        elif str[0] == '"':
            return str[1:]
        elif str[len(str) - 1] == '"':
            return str[:len(str) - 1]
        else:
            return str


if __name__ == "__main__":
    HBNBCommand().cmdloop()
