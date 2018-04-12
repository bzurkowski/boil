import re

from boil.plate.manager import Manager
from boil.exceptions import PlateNotFound
from boil import runner
from boil.utils.display import display, display_list


class Command:

    def execute(self, args):
        raise NotImplementedError()


class ListPlates(Command):

    def execute(self, args):
        plate_names = self._list_plates()
        display("Available plates:", bold=True)
        display_list(sorted(plate_names))

    def _list_plates(self):
        return Manager().get_plate_names()


class SearchPlates(Command):

    def execute(self, args):
        phrase = args['<phrase>']
        plate_names = self._search_plates(phrase)
        num_found = len(plate_names)
        if num_found > 0:
            display("Found plates (%s):" % num_found, bold=True)
            display_list(sorted(plate_names))
        else:
            display("No plates found.")

    def _search_plates(self, phrase):
        plate_names = Manager().get_plate_names()
        return [name for name in plate_names if phrase in name]


class RunPlate(Command):

    def execute(self, args):
        plate_name = self._normalize_plate_name(args['<plate_name>'])
        try:
            runner.run_plate(plate_name)
        except PlateNotFound:
            display("Plate not found.", color='red')

    def _normalize_plate_name(self, name):
        return re.sub(r"\W", '_', name)
