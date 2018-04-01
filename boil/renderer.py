import os


class Renderer:

    def __init__(self, env, vars, target_dir):
        self.env = env
        self.vars = vars
        self.target_dir = target_dir

    def run(self):
        for template_path in self.env.list_templates():
            self._render_template(template_path)

    def _render_template(self, template_path):
        template = self.env.get_template(template_path)
        target_path = self._get_target_path(template_path)
        self._ensure_target_dir(target_path)
        self._render_target(template, target_path)

    def _get_target_path(self, template_path):
        target_path = os.path.join(self.target_dir, template_path)
        target_path_template = self.env.from_string(target_path)
        target_path = target_path_template.render(self.vars)
        if target_path.endswith('.j2'):
            target_path = os.path.splitext(target_path)[0]
        return target_path

    def _ensure_target_dir(self, target_path):
        target_dir = os.path.dirname(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

    def _render_target(self, template, target_path):
        with open(target_path, 'w') as target:
            target.write(template.render(self.vars))
