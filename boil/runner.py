import os

from boil.plate.environment import Environment
from boil.plate.manager import Manager
from boil.plate.renderer import Renderer
from boil.common.filters import humanize
from boil.utils.display import display
from boil.vars.loader import VariableLoader


def run_plate(plate_name):
    plate = Manager().get_plate(plate_name)
    env = Environment(plate)

    display("Initializing new %s. Please provide the following variables:"
            % humanize(plate_name))

    vars_loader = VariableLoader(plate.vars)
    vars = vars_loader.get_vars()

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display("Done!", color='green')
