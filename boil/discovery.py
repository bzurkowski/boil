import pkg_resources


def load_plates():
    plates = {}
    for entry_point in pkg_resources.iter_entry_points('boil.plates'):
        plates[entry_point.name] = entry_point.load()


plates = load_plates()


def get_plate(plate_name):
    return plates[plate_name]


def list_plates():
    return plates.keys()


def search_plates(phrase):
    plate_names = list_plates()
    return [plate_name for plate_name in plate_names if phrase in plate_name]
