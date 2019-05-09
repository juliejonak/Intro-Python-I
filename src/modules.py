"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)

# import fileinput
# for line in fileinput.input():
#     print(line)

# Print out the OS platform you're using:
# YOUR CODE HERE
if sys.platform.startswith('linux'):
    print('Your platform is Linux')
elif sys.platform.startswith('win32'):
    print('Your platform is Windows')
elif sys.platform.startswith('darwin'):
    print('Your platform is Mac OS X')
else:
    print('Your platform is unidentified')

# Print out the version of Python you're using:
# YOUR CODE HERE

print('Your current version of Python is: ' + sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('The current process user id is: ' + str(os.geteuid()) + '. The current group id is: ' + str(os.getgid()) + '.')

# Print the current working directory (cwd):
# YOUR CODE HERE
print('The current working directory is: ' + str(os.getcwd()))

# Print out your machine's login name
# YOUR CODE HERE
print('Your current login name is: ' + str(os.getlogin()))