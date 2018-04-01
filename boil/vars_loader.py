from boil.utils.display import prompt
from boil.filters import humanize


def get_vars(var_defs):
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

        value = prompt(prompt_msg)
        vars[var['name']] = value
    return vars
