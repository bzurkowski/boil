import os

from boil import environment
from boil.filters import humanize
from boil import plates
from boil.renderer import Renderer
from boil.utils.display import display, prompt
from boil import vars_loader


def run_plate(plate_name):
    plate_module = plates.get(plate_name)

    display("Initializing new %s. Please provide the following variables:"
            % humanize(plate_name))

    env = environment.get(plate_module)
    vars = vars_loader.get_vars(plate_module.VARS)

    renderer = Renderer(env, vars, target_dir=os.getcwd())
    renderer.run()

    display("Done!", color='green')
