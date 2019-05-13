# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables
# Better reading: https://www.datacamp.com/community/tutorials/scope-of-variables-python , https://www.programiz.com/python-programming/global-keyword


# When you use a variable in a function, it's local in scope to the function.
x = 12

def changeX():
    global x
    x = 99

changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)

outer()
# OR can set y to global within inner(), but then need a print(y) after calling outer