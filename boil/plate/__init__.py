from boil.vars import parse_vars


class Plate:

    def __init__(self, module):
        self.module = module
        self._load_module_data()

    def _load_module_data(self):
        self.name = self.module.__name__
        self.vars = self._load_vars()
        self.filters = self._load_filters()

    def _load_vars(self):
        if hasattr(self.module, 'VARS'):
            return parse_vars(self.module.VARS)
        return []

    def _load_filters(self):
        if hasattr(self.module, 'FILTERS'):
            return self.module.FILTERS
        return {}
