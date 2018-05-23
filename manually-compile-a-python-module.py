# The python interpreter is stack-based and once source is compiled corresponding .pyc are ready in the same directory (in case of python 2.x). With python 3.x a new __pycache__ directory is created for the source and all compiled Bytecode files are placed underneath.
# The interpreter reads the binary file and executes the instructions (opcodes) one at a time.

import py_compile

py_compile.compile('hello-world.py')
