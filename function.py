
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
