"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string


# This returns all the values, separated by spaces
print(x, y, z)

# But we can specify separation by commas, for example:
print(x, y, z, sep=', ')

# Or we can concat as a string:
print('I am ' + str(x) + ' years old and my favorite number is ' + str(y) + '. ' + z)

# We can use string interpolation with the modulo operator %, but str.format() is preferred.

print('I am %i years old and my favorite number is %f. %s' % (x, y, z))

# We can also use str.format() to print a string with variable data:

print('I am {} years old and my favorite number is {}. {}'.format(x, y, z))

# We can even reference the variables in any order by referencing their index within the final parenthesis:

print('I am {1} years old and my favorite number is {2}. {0}'.format(z, x, y))

# As an added bonus, you can pass in objects to reference as parameters between braces:

person = { 'name': 'Julie', 'age': 26 }
print('Hi! My name is {name} and I am {age} years old.'.format(name=person['name'], age=person['age']))

# Even simpler, we can use ** to indicate the dictionary referencing keys:

print('Hi! My name is {name} and I am {age} years old.'.format(**person))

# f-strings are formatted string literals. They are strings that start with an f at the beginning and utilize curly brace variables inside, like so:

print(f'x is {x}, y is {y}, and z says: {z}.')

# This is much simpler but equally power to string.format(). You can also call functions and expressions within the curly braces:

def add(x, y):
    return x + y

print(f'{x} plus {y} equals {add(x, y)}. Plus, {z}')

# Learn more at: https://realpython.com/python-f-strings/