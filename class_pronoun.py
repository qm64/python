#!/usr/bin/env python3
"""Example use of metaclass to get the name of the enclosing class definition.
   Essentially, a python pronoun for "What class is this code defined in?"

   This avoids the proliferation of string literals in boilerplate, which have
   to be replaced, and are often missed.
"""

class MetaClass(type):
    """Return a class object with the __class__ attribute equal to the class object.
    This allows interesting things within the class, such as __class__.__name__,
    which are otherwise not available.

    This class is used as a metaclass by including it in the class definition:

        class SomeClass(object, metaclass=MetaClass):

    Then within the class, attributes of the class can be accessed, such as
    __class__.__name__. This is different from type(self).__class__.__name__,
    as the latter gives the class of self, which may not be the same as the
    surrounding class definition, due to inheritance.
    """
    def __new__(cls, name, bases, attrs):
        attrs['__class__'] = name
        return type.__new__(cls, name, bases, attrs)

# Base case
class A(object, metaclass=MetaClass):
    def __init__(self):
        print('In class A, self is type %s' % type(self).__name__)
        print('In class A, __class__.__name__ is %s' % __class__.__name__)

# Inherited case. Also calls init of parent, for comparison
class B(A):
    def __init__(self):
        print('In class B, self is type %s' % type(self).__name__)
        print('In class B, __class__.__name__ is %s' % __class__.__name__)
        # This is the same as: super(B, self).__init__()
        super().__init__()

# Now create a B() object, to demonstrate.
X = B()

"""
Output:

In class B, __class__.__name__ is B
In class A, __class__.__name__ is A
"""
