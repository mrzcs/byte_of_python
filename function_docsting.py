def print_max(x, y):
    '''Prints the max of two numbers.

    The two values must be integers.'''
    x = int(x)
    y = int(y)

    if x> y:
        print(x, 'is max')
    else:
        print(y, 'is max')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)