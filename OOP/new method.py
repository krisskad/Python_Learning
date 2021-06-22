"""
Whenever a class is instantiated __new__ and __init__ methods are called. __new__ method will be called when an object
is created and __init__ method will be called to initialize the object. In the base class object, the __new__ method is
defined as a static method which requires to pass a parameter cls. cls represents the class that is needed to be instantiated,
and the compiler automatically provides this parameter at the time of instantiation.


Syntax:
class class_name:
    def __new__(cls, *args, **kwargs):
        statements
        .
        .
        return super(class_name, cls).__new__(cls, *args, **kwargs)
"""


class A:
    pass


print(help())
