import os

from boil.utils.file_utils import ensure_dir


class Renderer:

    def __init__(self, env, vars):
        self._env = env
        self._vars = vars

    def render(self, target_dir):
        for template_path in self._env.list_templates():
            self._render_template(template_path, target_dir)

    def _render_template(self, template_path, target_dir):
        template = self._env.get_template(template_path)

        target_path = os.path.join(target_dir, template_path)

        target_path_template = self._env.from_string(target_path)
        target_path = target_path_template.render(self._vars)

        if target_path.endswith('.j2'):
            target_path = os.path.splitext(target_path)[0]

        ensure_dir(target_path)

        with open(target_path, 'w') as target:
            target.write(template.render(self._vars))
