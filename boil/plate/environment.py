import jinja2

from boil.common import filters


class Environment(jinja2.Environment):

    def __init__(self, plate, **kwargs):
        self.plate = plate
        self._set_defaults(kwargs)
        loader = jinja2.PackageLoader(plate.module_name)
        super(Environment, self).__init__(loader=loader, **kwargs)
        self._setup_filters()

    def _set_defaults(self, kwargs):
        kwargs.setdefault('keep_trailing_newline', True)

    def _setup_filters(self):
        self.filters.update(filters.PLATE_FILTERS)
        self.filters.update(self.plate.filters)
