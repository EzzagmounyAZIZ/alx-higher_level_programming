#!/usr/bin/python3
def magic_calculation(a, b):
    add = None
    sub = None

    if a < b:
        if add is None:
            from magic_calculation_102 import add as magic_add
            add = magic_add
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        if sub is None:
            from magic_calculation_102 import sub as magic_sub
            sub = magic_sub
        return sub(a, b)
