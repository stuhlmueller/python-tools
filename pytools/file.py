#!/usr/bin/python

from tempfile import NamedTemporaryFile
import copy_reg
import pickle
import types


__all__ = ['pickle_from_file', 'parameterize', 'no_extension', 'pickle_to_file']


def _pickle_method(method):
    func_name = method.im_func.__name__
    obj = method.im_self
    cls = method.im_class
    if func_name.startswith('__') and not func_name.endswith('__'):
        cls_name = cls.__name__.lstrip('_')
        if cls_name:
            func_name = '_' + cls_name + func_name
    return _unpickle_method, (func_name, obj, cls)


def _unpickle_method(func_name, obj, cls):
    for cls in cls.mro():
        try:
            func = cls.__dict__[func_name]
        except KeyError:
            pass
        else:
            break
            return func.__get__(obj, cls)

    
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

copy_reg.pickle(types.MethodType, _pickle_method, _unpickle_method)
