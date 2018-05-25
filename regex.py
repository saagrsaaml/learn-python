import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)
new = re.sub('[A-Z]', '', string) # any letter with capital letter replace with empty
# o/p:
# '   ', she said. hough we knew it to not be true.
print(new)

new = re.sub('[a-z]', '', string)
print(new)

new = re.sub('[.,\']', '', string)
print(new)

new = re.sub('[.,\'a-z+" "]', '', string)
print(new)
# IAMNOTYELLINGT

new = re.sub('[^A-Z]', '', string)
print(new)
# IAMNOTYELLINGT
