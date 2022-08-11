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
        """ cmd function that we'll override to intercept incomming commands
        and return standardly parsed commands for easr of use
        """

        if '.' in line and '(' in line and ')' in line:
            """ intercepts commands with .() notation and extracts the
            args into one strings"""
            toks = re.split(r'\.|\(|\)', line)

            payload = toks[2].strip('"').replace(',', ' ')
            # if payload[0] == '{' and payload[-1] == '}':
            payload = self.dict_to_str(payload)

            newline = toks[1] + ' ' + toks[0] + ' ' + payload
            if payload == '':
                line = (toks[1], toks[0], newline)
                # print("======== line no payload =======")
                # print(line)
            else:
                line = (toks[1], toks[0] + " " + payload, newline)
                # print("========= line with payload ===========")
                # print(line)

            if toks[1] == 'count':
                self.count(toks[0])
                return cmd.Cmd.parseline(self, '')
            # print("====== line =====")
            # print(line)
            return line
        else:
            """ intercepts regular all string commands to remove any quotes
            to output standadized text
            """
            args = line.split(" ")
            # print("intercepted straight one")
            # pprint(args)
            payload = []
            if len(args) > 2:
                payload = args[2:]
                payload = self.list_to_string(payload)
                # print("==== sanitized payload =====")
                # print(payload)
                newline = args[0] + ' ' + args[1] + ' ' + payload
                line = (args[0], args[1] + " " + payload, newline)
                # print("====== line =====")
                # print(line)
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

    def do_test(self, args):
        """test args parsing"""
        print(args)

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
        argarr = args.split(" ")
        # print("=========== create args ++++++++++++++++++++")
        # pprint(argarr)
        # print("=========== create args ++++++++++++++++++++")
        c_name = argarr[0]
        if not c_name:
            print("** class name missing **")
            return
        elif c_name not in storage.classes():
            print("** class doesn't exist **")
            return
        new_instance = storage.classes()[c_name](argarr)
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
        """Updates an onbject with new args overwriting the previous ones """
        new = args.split(" ")
        if len(new) == 1:
            print(" insufficient args ,instance id might be missing")
        if len(new) == 2:
            print("insufficient arguments , needs at least 1 key value pair ")
        if len(new) > 3:
            self.update_instance(new)
        storage.save()

    def update_instance(self, args):
        """"helper function to update an instance """
        name = args[0]
        id = args[1]
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
        # if valid key is found we'll search for it be key on the storage
        # class and call te update method in the base_model
        # remeber to pass in the object itself in the instance parameter
        # <storage.all()[key]> the other param <args> is from user input
        try:
            storage.all()[key].update(args, storage.all()[key])

        except KeyError:
            print("** no instance found **")

    def help_update(self):
        """Help information for the update class."""
        print("Updates an object woth new information")
        print("Usage: update <className> <id> <attName> <attValue>\n")
        print("Usage: update <className> <id> <attName> <attValue>\n")

    def dict_to_str(self, dict):
        """"converts  a dictionary like string to string for easier parsing"""
        dictlist = dict.split(' ')
        newstr = ""
        for idx in range(len(dictlist)):
            newword = ""
            for word in dictlist[idx]:
                if not word == '"' and not word == '' and not word == "'" and\
                    not word == "}" and not word == "{"   \
                        and not word == ":":
                    newword = "".join([newword, word])
            if len(newword) > 0:
                newstr += str(newword) + " "

        newstr = newstr.strip()
        # print("===== dict list =========")
        # print(newstr)
        return newstr

    def list_to_string(self, list):
        """ takes a list and spits out a string comprised of each
        list item separated by blank space  """
        newstr = ""
        for idx in range(len(list)):
            word = list[idx]
            newword = ""
            for chr in word:
                if not chr == '"' and not chr == '' and not chr == "'":
                    newword = "".join([newword, chr])

            # print("===== new word =========")
            # print(newword)
            if len(newword) > 0:
                newstr += str(newword) + " "

        newstr = newstr.strip()
        # print("===== list to str =========")
        # print(newstr)
        return newstr

    def strip_quotes(self, str):
        """removes quotes from strings for easier parsing"""
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
