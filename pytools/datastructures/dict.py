#!/usr/bin/python

from collections import defaultdict


__all__ = ['nested_dict']


def nested_dict():
    return defaultdict(nested_dict)
