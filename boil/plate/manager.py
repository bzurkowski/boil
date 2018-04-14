import pkg_resources

from boil.exceptions import PlateNotFound
from boil.plate import Plate
from boil.utils.misc import singleton


@singleton
class Manager:

    ENTRY_NAMESPACE = 'boil.plates'

    def __init__(self):
        self._plates = self._load_plates()

    def get_plate(self, plate_name):
        if plate_name not in self._plates:
            raise PlateNotFound(name=plate_name)
        return self._plates[plate_name]

    def get_plate_names(self):
        return self._plates.keys()

    def _load_plates(self):
        plates = {}
        for entry_point in self._iter_entry_points():
            plates[entry_point.name] = Plate(entry_point.load())
        return plates

    def _iter_entry_points(self):
        return iter(pkg_resources.iter_entry_points(self.ENTRY_NAMESPACE))
