#!/usr/bin/python3
"""Console module."""

import cmd


class HBNBCommand(cmd.Cmd):
    """The HBNB console functionalities."""
    prompt = '(hbnb)'

    def do_quit(self, command):
        """ Method that exit the HBNB console."""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit."""
        print("Exits the program with formatting")

    def do_EOF(self, command):
        """Handles EOF to exit program."""
        exit()

    def help_EOF(self):
        """Prints the help documentation for EOF."""
        print("Exits the program without formatting")

    def emptyline(self):
        """Overrides the CMD emptline method."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
