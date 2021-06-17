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
print(dir(A))
print(help(A))
