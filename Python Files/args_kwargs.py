def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(1, 2, 3, a='apple', b='banana')

"""
The * before args and ** before kwargs are called "unpacking operators". 
They tell Python to unpack the arguments passed to the function into a tuple (args) and a dictionary 
(kwargs) so that they can be passed on to another function or used in some other way.
"""