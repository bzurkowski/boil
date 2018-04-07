from boil.plate.manager import Manager
from boil.exceptions import PlateNotFound
from boil import runner
from boil.utils.display import display


class Command:

    def execute(self, args):
        raise NotImplementedError()


class ListPlates(Command):

    def execute(self, args):
        plate_names = self._list_plates()
        display("Available plates:")
        display('\n'.join(plate_names))

    def _list_plates(self):
        return Manager().list_plates()


class SearchPlates(Command):

    def execute(self, args):
        phrase = args['<phrase>']
        plate_names = self._search_plates(phrase)
        num_found = len(plate_names)
        if num_found > 0:
            display("Found plates (%s):" % num_found)
            display('\n'.join(plate_names))
        else:
            display("No plates found.")

    def _search_plates(self, phrase):
        return Manager().search_plates(phrase)


class RunPlate(Command):

    def execute(self, args):
        plate_name = args['<plate_name>']
        try:
            runner.run_plate(plate_name)
        except PlateNotFound:
            display.display("Plate not found.", color='red')
