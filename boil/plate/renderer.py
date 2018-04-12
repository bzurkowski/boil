import os

from boil.exceptions import ArtifactAlreadyExists
from boil.utils.file_utils import copy_tree, temp_dir


class Renderer:

    def __init__(self, template_renderer, overwrite=False):
        self.template_renderer = template_renderer
        self.overwrite = overwrite

    def render(self, target_dir):
        with temp_dir() as tmp_dir:
            self.template_renderer.render(tmp_dir)

            if not self.overwrite:
                target_names = os.listdir(target_dir)
                for name in os.listdir(tmp_dir):
                    if name in target_names:
                        raise ArtifactAlreadyExists(name=name)

            copy_tree(tmp_dir, target_dir)
