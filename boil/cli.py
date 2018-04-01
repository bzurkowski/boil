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


def main():
    args = docopt(__doc__)
    plate_name = args['<plate_name>']

    plate = plates.get_plate(plate_name)

    display = Display()

    vars = {}
    for var in plate.VARS:
        name = filters.humanize(var['name'])
        example = var.get('example', var.get('default'))
        prompt_str = "%s [%s]:\n" % (name, example)
        value = display.prompt(prompt_str)
        vars[var['name']] = value

    env = get_environment(plate)

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()
