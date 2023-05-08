#!/usr/bin/python3

"""
Module Description:
This module contains a sample class MyClass.

Class Description:
MyClass is a simple class that represents an example object.

Function Description:
my_function is a sample function that prints a message.

Usage:
Instantiate an object of MyClass and call its methods.
Call my_function to print a message.
"""

class MyClass:
    """
    MyClass is a simple class that represents an example object.
    """

    def __init__(self, name):
        """
        Initialize MyClass object with a name.
        """
        self.name = name

    def get_name(self):
        """
        Get the name of the object.
        """
        return self.name

    def set_name(self, new_name):
        """
        Set the name of the object.
        """
        self.name = new_name


def my_function():
    """
    A sample function that prints a message.
    """
    print("This is a sample function.")


if __name__ == "__main__":
    # Create an instance of MyClass
    obj = MyClass("Sample Object")
    print(obj.get_name())

    # Call my_function
    my_function()
