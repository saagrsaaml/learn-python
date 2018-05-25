# The first statement in the body of a function is usually a string, which can be accessed with
# function_name.__doc__
# This statement is called Docstring.
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")

print("The docstring of the function Hello: " + Hello.__doc__)
# o/p
# The docstring of the function Hello:  Greets a person

# positional arguments
def my_function(str1, str2):
    print(str1+str2)
my_function('go','now')

# default arguments
def my_function(name='sagar samal', age='27'):
    print('My name is', name, 'and my age is', age)
my_function('sagar')

# keyword arguments
def my_function(name='sagar samal', age='27'):
    print('My name is', name, 'and my age is', age)
my_function(age = '22', name = 'hero')

# infinite arguments
# *people represents array of people elements
def print_people(*people, **details):
    print(people)
    print(details)
print_people('sagar','samal', home="samakhusi", college= 'NCIT')
