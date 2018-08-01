#!/usr/bin/env python3
"""Demo getting the class name of a class within the class code."""

class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['__class__'] = name
        return type.__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    def __init__(self):
        print("This MyClass class is %s" % __class__.__name__)

x = MyClass()

"""
Output:

This MyClass class is MyClass
"""