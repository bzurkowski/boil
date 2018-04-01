import pkg_resources


def load_plates():
    plates = {}
    for entry_point in pkg_resources.iter_entry_points('boil.plates'):
        plates[entry_point.name] = entry_point.load()
    return plates
