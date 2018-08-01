# Python snippets

#################################

class MetaClass(type):
    """Return a class object with the __class__ attribute equal to the class object.
    This allows interesting things within the class, such as __class__.__name__,
    which are otherwise not available.

    This class is used as a metaclass by including it in the class definition:

        class SomeClass(object, metaclass=MetaClass):

    Then within the class, attributes of the class can be accessed, such as
    __class__.__name__. This is different from type(self).__name__,
    as the latter gives the class of self, which may not be the same as the
    surrounding class definition, due to inheritance.
    """
    def __new__(mcs, name, bases, attrs):
        attrs['__class__'] = name
        return type.__new__(mcs, name, bases, attrs)

#################################
