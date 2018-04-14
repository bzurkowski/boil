class Variable:

    def __init__(self, name, default=None, example=None):
        self.name = name
        self.default = default
        self.example = example


def parse_vars(raw_vars):
    return [Variable(**raw_var) for raw_var in raw_vars]
