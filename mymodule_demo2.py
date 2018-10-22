from mymodule import say_hi, __version__
#from mymodule import * # will import all public names such as say_hi but would not import __version__

say_hi()
print('Version:', __version__)