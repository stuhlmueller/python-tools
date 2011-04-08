#!/usr/bin/python

from collections import defaultdict


__all__ = ['nested_dict', 'print_nested_dict']


def nested_dict():
    return defaultdict(nested_dict)

def print_nested_dict(dic, ind=0):
    for (k, v) in dic.items():
        print " "*ind + str(k) + ":",
        if type(v) == type(dic):
            print
            print_nested_dict(v, ind+2)
        else:
            print v
