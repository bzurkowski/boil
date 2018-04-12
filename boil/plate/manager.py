import pkg_resources

from boil.exceptions import PlateNotFound
from boil.plate import Plate
from boil.utils.misc import singleton


@singleton
class Manager:

    ENTRY_NAMESPACE = 'boil.plates'

    def __init__(self):
        self.plates = self._load_plates()

    def get_plate(self, plate_name):
        if plate_name not in self.plates:
            raise PlateNotFound(plate_name=plate_name)
        return self.plates[plate_name]

    def get_plate_names(self):
        return self.plates.keys()

    def _load_plates(self):
        plates = {}
        for entry_point in self._iter_entry_points():
            plates[entry_point.name] = Plate(entry_point.load())
        return plates

    def _iter_entry_points(self):
        return iter(pkg_resources.iter_entry_points(self.ENTRY_NAMESPACE))
