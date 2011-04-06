#!/usr/bin/python

from StringIO import StringIO


__all__ = ['IncStringIO']


class IncStringIO(StringIO):
    def __init__(self, *args, **kwargs):
        StringIO.__init__(self, *args, **kwargs)
        self.read_pos = 0
    
    def read_new(self):
        total = self.getvalue()
        increment = total[self.read_pos:]
        self.read_pos = len(total)
        return increment
    
    def __str__(self):
        return self.getvalue()
