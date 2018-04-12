from boil.template import renderer as tmpl_renderer
from boil.utils.file_utils import copy_tree, temp_dir


class Renderer:

    def __init__(self, env, vars, target_dir):
        self.env = env
        self.vars = vars
        self.target_dir = target_dir

    def run(self):
        with temp_dir() as tmp_dir:
            renderer = tmpl_renderer.Renderer(self.env, self.vars, tmp_dir)
            renderer.run()

            copy_tree(tmp_dir, self.target_dir)
