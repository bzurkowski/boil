import os

from boil.common.filters import humanize
from boil.plate.manager import Manager
from boil.plate.renderer import Renderer
from boil.template.environment import Environment
from boil.template import renderer as tmpl_renderer
from boil.utils.display import display
from boil.vars.loader import VariableLoader


def run_plate(plate_name):
    plate = Manager().get_plate(plate_name)

    display("Initializing new %s. Please provide the following variables:"
            % humanize(plate_name))

    vars_loader = VariableLoader(plate.vars)
    vars = vars_loader.get_vars()

    env = Environment(plate.module_name)

    template_renderer = tmpl_renderer.Renderer(env, vars)

    plate_renderer = Renderer(template_renderer)
    plate_renderer.render(os.getcwd())

    display("Done!", color='green')
