import os

from boil.utils.file_utils import ensure_dir


class Renderer:

    def __init__(self, env, vars):
        self.env = env
        self.vars = vars

    def render(self, target_dir):
        for template_path in self.env.list_templates():
            self._render_template(template_path, target_dir)

    def _render_template(self, template_path, target_dir):
        template = self.env.get_template(template_path)

        target_path = os.path.join(target_dir, template_path)

        target_path_template = self.env.from_string(target_path)
        target_path = target_path_template.render(self.vars)

        if target_path.endswith('.j2'):
            target_path = os.path.splitext(target_path)[0]

        ensure_dir(target_path)

        with open(target_path, 'w') as target:
            target.write(template.render(self.vars))
