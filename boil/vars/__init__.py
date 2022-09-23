class Variable:
    def __init__(self, name, required=False, default=None, example=None):
        self.name = name
        self.required = required
        self.default = default
        self.example = example


def parse_vars(var_defs):
    return [Variable(**var_def) for var_def in var_defs]
