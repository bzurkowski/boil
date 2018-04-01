"""Boil

Usage:
  boil new <plate_name>
  boil list
"""

from docopt import docopt

from boil import discovery
from boil import runner
from boil.utils import display


def main():
    args = docopt(__doc__)

    if args['list']:
        list_plates()
    elif args['new']:
        plate_name = args['<plate_name>']
        run_plate(plate_name)


def list_plates():
    plates = discovery.load_plates()
    plate_names = plates.keys()
    display.display("Available plates:")
    display.display('\n'.join(plate_names))


def run_plate(plate_name):
    runner.run_plate(plate_name)
