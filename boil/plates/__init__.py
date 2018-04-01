from boil.utils.import_utils import import_module


def get(plate_name):
    return import_module(__name__, plate_name)
