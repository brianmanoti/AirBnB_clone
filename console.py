#!/usr/bin/python3
""" Console Module """
import cmd
class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '
     def do_quit(self, command):
        """ Method to exit the HBNB console"""
        exit()
    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
