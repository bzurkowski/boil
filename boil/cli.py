"""Boil

Usage:
  boil new <plate_name>
"""

import os
import random

from docopt import docopt

from boil.environment import get_environment
from boil.renderer import Renderer


def main():
    args = docopt(__doc__)
    plate_name = args['<plate_name>']

    env = get_environment(plate_name)
    env.globals['app_name'] = ''.join(
        [random.choice('abcde') for _ in range(10)])

    renderer = Renderer(env, target_dir=os.getcwd())
    renderer.run()
