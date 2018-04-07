import os

from boil.discovery import PlateManager
from boil.environment import PlateEnvironment
from boil.common.filters import humanize
from boil.renderer import Renderer
from boil.utils.display import display
from boil.vars.loader import VariableLoader


def run_plate(plate_name):
    plate_manager = PlateManager()
    plate = plate_manager.get_plate(plate_name)

    env = PlateEnvironment(plate)

    display("Initializing new %s. Please provide the following variables:"
            % humanize(plate_name))

    vars_loader = VariableLoader(plate.vars)
    vars = vars_loader.get_vars()

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display("Done!", color='green')
