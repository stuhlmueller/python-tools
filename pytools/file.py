#!/usr/bin/python

import pickle
from tempfile import NamedTemporaryFile

__all__ = ['pickle_from_file', 'parameterize', 'no_extension', 'pickle_to_file']


def parameterize(template_filename, parameters):
    """
    Returns a temporary filename that corresponds to a file that is
    like the given file with parameter values instead of string
    interpolation placeholders.
    """
    template_file = open(template_filename)
    template = template_file.read()
    template_file.close()
    instance_file = NamedTemporaryFile(delete=False)
    instance_file.write(template % parameters)
    instance_file.close()
    return instance_file.name


def no_extension(filename):
    return "".join(filename.split(".")[:-1])


def pickle_to_file(data, filename):
    f = open(filename, "w")
    pickle.dump(data, f)
    f.close()

    
def pickle_from_file(filename):
    f = open(filename, "r")
    obj = pickle.load(f)
    f.close()
    return obj
