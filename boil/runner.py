import os

from boil.discovery import PlateManager
from boil import environment
from boil.common.filters import humanize
from boil.renderer import Renderer
from boil.utils.display import display
from boil.vars.loader import VariableLoader


def run_plate(plate_name):
    plate = PlateManager().get_plate(plate_name)

    display("Initializing new %s. Please provide the following variables:"
            % humanize(plate_name))

    env = environment.get(plate)

    vars_loader = VariableLoader(plate.vars)
    vars = vars_loader.get_vars()

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display("Done!", color='green')
