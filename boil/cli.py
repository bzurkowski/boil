"""Boil

Usage:
  boil new <plate_name>
"""

from docopt import docopt

from boil import runner


def main():
    args = docopt(__doc__)
    plate_name = args['<plate_name>']

    runner.run_plate(plate_name)
