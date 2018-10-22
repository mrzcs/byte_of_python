age = 20
name = 'Kevin'

# using index
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

# numbers are optional
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# name the parameters
print('{name} was {age} years old when he wrote this book'.format(name=name, age=age))
print('Why is {name} playing with that python?'.format(name=name))

# f-strings (version>3.6)
print(f'{name} was {age} years old when he wrote this book')
print(f'Why is {name} playing with that python?')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores(_) with the text centered
# (^) to 11 width
print('{0:_^11}'.format('hello'))
# keyword-based
print('{name} wrote {book}'.format(name='Nancy', book='A Byte of PYthon'))

# by default, print ends with new line (\n)
# to prevent new line character, ends with blank
print('a', end='')
# ends with space
print('b', end=' ')
print('c')