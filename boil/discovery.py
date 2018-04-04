import pkg_resources

from boil.exceptions import PlateNotFound
from boil.utils import misc


@misc.singleton
class PlateManager:

    def __init__(self):
        self.plates = self._load_plates()

    def get_plate(self, plate_name):
        if plate_name not in self.plates:
            raise PlateNotFound(plate_name=plate_name)
        return self.plates[plate_name]

    def list_plates(self):
        return self.plates.keys()

    def search_plates(self, phrase):
        return [plate_name for plate_name in self.list_plates()
                if phrase in plate_name]

    def _load_plates(self):
        plates = {}
        for entry_point in pkg_resources.iter_entry_points('boil.plates'):
            plates[entry_point.name] = entry_point.load()
        return plates
