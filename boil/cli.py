"""Boil

Usage:
  boil new <plate_name>
"""

import os
import random

from docopt import docopt

from boil import plates
from boil import filters
from boil.environment import get_environment
from boil.renderer import Renderer
from boil.utils.display import Display
from boil.vars_loader import VarsLoader


def main():
    args = docopt(__doc__)
    plate_name = args['<plate_name>']

    plate = plates.get_plate(plate_name)

    display = Display()

    display.display("Initializing new %s. Please provide the following variables:" % filters.humanize(plate_name))

    vars_loader = VarsLoader()
    vars = vars_loader.get_vars(plate.VARS)

    env = get_environment(plate)

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display.display("Done!", color='green')
