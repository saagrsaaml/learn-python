print('C:\some\name') # here \n means newline!

# o/p :
###########
# C:\some #
# ame     #
###########

# If you don’t want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote:

print(r'C:\some\name') # note the r before the quote

# o/p :
################
# C:\some\name #
################

# String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
# End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line.

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Sting Concatination

print(3 * 'un' + 'ium') # 3 times 'un', followed by 'ium'

print('Py''thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'Py'
# print(prefix 'thon') error
print(prefix + 'thon') #concatenate variables or a variable and a literal, with +:

print(len(text))

word = 'Python'
print(word[5]) # character in position 5
# since -0 is the same as 0, negative indices start from -1.
print(word[-1]) # last character
# Slicing
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
# start is always included, and the end always excluded.
# s[:i] + s[i:] is always equal to s:
print(word[:2] + word[2:])
# an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
