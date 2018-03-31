from boil.utils.import_utils import import_module


def get_plate(name):
    return import_module(__name__, name)
