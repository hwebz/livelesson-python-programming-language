x = 42

def spam():
	print('x is', x)

def run():
	print('Calling spam')
	spam()

print('Running')
run()

import math
math.cos(2)
math.sqrt(4)

from simple import run
import simple
run = simple.run
run()

from simple import run, x # Python cache at the first time of any lib (del module before import to del cache)
# x = 13 # not affect to local variable of simple on import statement
simple.x = 13 # Possible
sys.module['simple']
del sys.module['simple']

# If you are in another path of mobile want to be imported.
import sys
sys.path.append('..') # Go back directory
import simple

# Or change path of environment variable for python, after that you can import simple
# env PYTHONPATH=.. python
__name__
simple.__name__