"""

Constructor is the special method within class used to set initial attributes or behaviour of the object.
It will execute whenever we create the object.

Syntax:
    def __init__(self):
        pass

"""


class A:
    """
    Constructor

    """

    def __init__(self, A, B):
        self.a = A
        self.b = B
        print(self.a + self.b)


obj = A(10,20)

# output
# 30
