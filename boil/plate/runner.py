import os

from boil.exceptions import ArtifactAlreadyExists
from boil.template.renderer import TemplateRenderer
from boil.template.environment import Environment
from boil.utils.file_utils import copy_tree, temp_dir
from boil.vars.loader import VariableLoader


class PlateRunner:

    """
    This is the primary class responsible for running a plate. It generates
    the project structure inside a temporary directory and copies its contents
    to the destination directory afterwards, ensuring that there are no
    artifact conflicts.
    """

    def __init__(self, plate, target_dir, overwrite=False):
        self._plate = plate
        self._target_dir = target_dir
        self._overwrite = overwrite

    def run_plate(self):
        vars_loader = VariableLoader(self._plate.vars)
        vars = vars_loader.get_vars()

        env = Environment(self._plate.module_name)

        with temp_dir() as tmp_dir:
            TemplateRenderer(env, vars).render(tmp_dir)

            if not self._overwrite:
                target_names = os.listdir(self._target_dir)
                for name in os.listdir(tmp_dir):
                    if name in target_names:
                        raise ArtifactAlreadyExists(name=name)

            copy_tree(tmp_dir, self._target_dir)
