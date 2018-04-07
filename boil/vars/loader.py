from boil.common.filters import humanize
from boil.utils.display import prompt


class VariableLoader:

    def __init__(self, var_defs):
        self.var_defs = var_defs

    def get_vars(self):
        collected_vars = {}
        for var in self.var_defs:
            collected_vars[var['name']] = self._prompt_var(var)
        return collected_vars

    def _prompt_var(self, var):
        prompt_msg = self._build_prompt_msg(var)
        return prompt(prompt_msg)

    def _build_prompt_msg(self, var):
        var_name = humanize(var['name'])
        example = var.get('example')
        default = var.get('default')

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
