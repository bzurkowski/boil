"""Boil

Usage:
  boil new <plate_name>
"""

import os
import random

from docopt import docopt

from boil import plates
from boil.environment import get_environment
from boil.renderer import Renderer


def main():
    args = docopt(__doc__)
    plate_name = args['<plate_name>']

    plate = plates.get_plate(plate_name)

    vars = {}
    for var in plate.VARS:
        example = var.get('example', var.get('default'))
        prompt_str = "%s [%s]:\n" % (var['name'], example)
        value = raw_input(prompt_str)
        vars[var['name']] = value

    env = get_environment(plate)
    env.globals.update(vars)

    renderer = Renderer(env, target_dir=os.getcwd())
    renderer.run()
