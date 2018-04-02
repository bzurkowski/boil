"""Boil

Usage:
    boil list
    boil search <phrase>
    boil new <plate_name>
    boil -h | --help
"""

from docopt import docopt

from boil import discovery
from boil.exceptions import PlateNotFound
from boil import runner
from boil.utils.display import display


def main():
    args = docopt(__doc__)

    if args['list']:
        list_plates()
    elif args['search']:
        phrase = args['<phrase>']
        search_plates(phrase)
    elif args['new']:
        plate_name = args['<plate_name>']
        run_plate(plate_name)


def list_plates():
    plates = discovery.list_plates()
    display("Available plates:")
    display('\n'.join(plates))


def search_plates(phrase):
    plates = discovery.search_plates(phrase)
    num_found = len(plates)
    if num_found > 0:
        display("Found plates (%s):" % num_found)
        display('\n'.join(plates))
    else:
        display("No plates found.")


def run_plate(plate_name):
    try:
        runner.run_plate(plate_name)
    except PlateNotFound:
        display.display("Plate not found.", color='red')
