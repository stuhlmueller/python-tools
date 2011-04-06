#!/usr/bin/python

import hashlib


__all__ = ['hash_digest']


def hash_digest(obj):
    return hashlib.sha224(obj).hexdigest()
