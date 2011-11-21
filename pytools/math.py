#!/usr/bin/python


__all__ = ['argmin', 'argmax']


def argmax(lst, func):
    mx, funcmx = None, None
    for val in lst:
        if (funcmx is None) or func(val) > funcmx:
            mx, funcmx = val, func(val)
    return mx

def argmin(lst, func):
    return argmax(lst, lambda x: -func(x))
