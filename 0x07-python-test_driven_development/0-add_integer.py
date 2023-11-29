#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
    """

    # Check if a is not an integer or float
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    # Check if b is not an integer or float
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Cast a and b to integers
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return a + b
