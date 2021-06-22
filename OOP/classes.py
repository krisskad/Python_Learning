"""
==========
Classes
==========
Definition:
    The combination of attributes and its behaviours called classes
    Where attributes are called data variables and behaviours are called method's or functions

Syntax:
    class ClassName:
        class_varible = 0

        def methods(self):
            pass
"""


class A:
    """
    Class Document
    """
    pass


print(A.__dict__)
print(A.__doc__)
print(A.__init__)

# It will print all the methods are available within class, some of methods are by default and some can be user defined
print(dir(A))

# It will print help doc
print(help(A))
