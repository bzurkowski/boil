import os

from boil.filters import humanize
from boil import plates
from boil import filters
from boil import environment
from boil.renderer import Renderer
from boil.utils.display import Display
from boil.vars_loader import VarsLoader


def run_plate(plate_name):
    display = Display()

    plate = plates.get_plate(plate_name)

    display.display("Initializing new %s. Please provide the following " \
                    "variables:" % filters.humanize(plate_name))

    env = environment.get_environment(plate)

    vars_loader = VarsLoader()
    vars = vars_loader.get_vars(plate.VARS)

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display.display("Done!", color='green')
