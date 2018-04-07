class Plate:

    def __init__(self, module):
        self.module = module
        self._load_module_data()

    def _load_module_data(self):
        self.name = self.module.__name__
        self.vars = self.module.VARS if hasattr(self.module, 'VARS') else []
        self.filters = {}
        if hasattr(self.module, 'FILTERS'):
            self.filters = self.module.FILTERS
