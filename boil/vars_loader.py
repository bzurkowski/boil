from boil.utils.display import Display
from boil.filters import humanize


class VarsLoader:

    def __init__(self):
        self.display = Display()

    def get_vars(self, var_defs):
        vars = {}
        for var in var_defs:
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

            value = self.display.prompt(prompt_msg)
            vars[var['name']] = value
        return vars
