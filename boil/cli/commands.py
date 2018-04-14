import os
import re

from boil.common.filters import humanize
from boil.exceptions import BoilError, PlateNotFound
from boil.plate.manager import PlateManager
from boil.plate.renderer import PlateRenderer
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
        return PlateManager().get_plate_names()


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
        plate_names = PlateManager().get_plate_names()
        return [name for name in plate_names if phrase in name]


class RenderPlate(Command):

    def execute(self, args):
        plate_name = self._normalize_name(args['<plate_name>'])
        target_dir = args['--target-dir'] or os.getcwd()

        display("Initializing new %s." % humanize(plate_name))
        try:
            self._render_plate(plate_name, target_dir)
            display("Done!", color='green')
        except PlateNotFound:
            display("Plate not found.", color='red')
        except BoilError as ex:
            display("An error ocurred while rendering a plate: %s" % str(ex),
                    color='red')

    def _normalize_name(self, name):
        return re.sub(r"\W", '_', name)

    def _render_plate(self, plate_name, target_dir):
        plate = PlateManager().get_plate(plate_name)
        PlateRenderer(plate, target_dir).render()
