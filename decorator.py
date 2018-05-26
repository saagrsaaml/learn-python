# A decorator in Python is any callable Python object that is used to modify a function or a class.
# A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class.
# The modified functions or classes usually contain calls to the original function "func" or class "C".
# Two different kinds of decorators in Python:
#    Function decorators
#    Class decorators

# Functions inside Functions

def f():

    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f()

# o/p
# This is the function 'f'
# I am calling 'g' now:
# Hi, it's me 'g'
# Thanks for calling me

#------------------------------------------------------------------------------#
print("-----------------------------------------------------------------------")
# Functions as Parameters

def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("This is the function 'f'")
    print("I am calling 'func' now:")
    func()
    print("func's real name is " + func.__name__) # returns 'real' name of func

f(g)
# o/p
# This is the function 'f'
# I am calling 'func' now:
# Hi, it's me 'g'
# Thanks for calling me
# func's real name is g
