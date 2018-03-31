import sys


def import_module(module_str, submodule=None):
    if submodule:
        module_str = '.'.join((module_str, submodule))
    __import__(module_str)
    return sys.modules[module_str]
