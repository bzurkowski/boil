from boil import discovery
from boil.exceptions import PlateNotFound
from boil import runner
from boil.utils.display import display


class Command:

    def execute(self, args):
        raise NotImplementedError()


class ListPlates(Command):

    def execute(self, args):
        plates = discovery.list_plates()
        display("Available plates:")
        display('\n'.join(plates))


class SearchPlates(Command):

    def execute(self, args):
        phrase = args['<phrase>']
        plates = discovery.search_plates(phrase)
        num_found = len(plates)
        if num_found > 0:
            display("Found plates (%s):" % num_found)
            display('\n'.join(plates))
        else:
            display("No plates found.")


class RunPlate(Command):

    def execute(self, args):
        plate_name = args['<plate_name>']
        try:
            runner.run_plate(plate_name)
        except PlateNotFound:
            display.display("Plate not found.", color='red')
