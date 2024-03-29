import os
import re

from boil.utils.file_utils import ensure_dir


class TemplateRenderer:

    PATH_EXCLUDE_PATTERNS = [r"^_includes\/.+"]

    def __init__(self, env, vars, target_dir):
        self._env = env
        self._vars = vars
        self._target_dir = target_dir

    def render(self):
        for template_path in self._env.list_templates():
            if self._is_valid_path(template_path):
                self._render_template(template_path)

    def _is_valid_path(self, template_path):
        for exclude_pattern in self.PATH_EXCLUDE_PATTERNS:
            if re.match(exclude_pattern, template_path):
                return False
        return True

    def _render_template(self, template_path):
        template = self._env.get_template(template_path)

        target_path = self._build_target_path(template_path)
        ensure_dir(target_path)

        with open(target_path, "wb") as target:
            target.write(template.render(self._vars).encode("utf8"))

    def _build_target_path(self, template_path):
        target_path = os.path.join(self._target_dir, template_path)

        target_path_template = self._env.from_string(target_path)
        target_path = target_path_template.render(self._vars)

        if target_path.endswith(".j2"):
            target_path = os.path.splitext(target_path)[0]
        return target_path
