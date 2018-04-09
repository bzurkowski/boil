class Variable:

    def __init__(self, name, default=None, example=None):
        self.name = name
        self.default = default
        self.example = example


def parse_vars(var_defs):
    return [Variable(**var_def) for var_def in var_defs]
