import sys # importing multiple modules  import sys, os -- bad instead
import os
from module import ClassA, ClassB # importing multiple classes from a module use


def my_function(one, two, # leave two lines between module importing and function or class declaration
                three, four, # arguments must be indented same way
                five, six):
    print("Hello World")


def my_function(): # leave two lines between two declaration of functions or classes
    print("second Function")


my_list = [1, 2, # must be indented same way
           3, 4,
           5, 6]
