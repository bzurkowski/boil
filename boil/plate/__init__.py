from boil.vars import parse_vars


class Plate:

    def __init__(self, module):
        self.module = module
        self._load_plate_data()

    def _load_plate_data(self):
        module_name = self.module.__name__

        self.name = module_name.split('.')[-1]
        self.module_name = module_name

        self.vars = []
        self.filters = {}

        if hasattr(self.module, 'VARS'):
            self.vars = parse_vars(self.module.VARS)

        if hasattr(self.module, 'FILTERS'):
            self.filters = self.module.FILTERS
