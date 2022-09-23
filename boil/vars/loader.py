from boil.common.filters import humanize
from boil.utils.display import display, prompt


class VariableLoader:
    def __init__(self, vars):
        self._vars = vars

    def get_vars(self):
        collected_vars = {}
        for var in self._vars:
            collected_vars[var.name] = self._collect_var(var)
        return collected_vars

    def _collect_var(self, var):
        prompt_msg = self._build_prompt_msg(var)
        value = prompt(prompt_msg)
        if not value:
            default = var.default
            if default:
                display("Using default: %s." % default)
                value = default
        while var.required and not value:
            display("Value required.", color="red")
            value = prompt(prompt_msg)
        return value

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
