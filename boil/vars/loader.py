from boil.common.filters import humanize
from boil.utils.display import prompt


class VariableLoader:

    def __init__(self, vars):
        self._vars = vars

    def get_vars(self):
        collected_values = {}
        for var in self._vars:
            collected_values[var.name] = self._collect_var(var)
        return collected_values

    def _collect_var(self, var):
        prompt_msg = self._build_prompt_msg(var)
        return prompt(prompt_msg)

    def _build_prompt_msg(self, var):
        var_name = humanize(var.name)
        example = var.example
        default = var.default

        hint = None
        if default:
            hint = default
        elif example:
            hint = "e.g. %s" % example

        prompt_msg = None
        if hint:
            prompt_msg = "%s [%s]:\n" % (var_name, hint)
        else:
            prompt_msg = "%s:\n" % var_name
        return prompt_msg
