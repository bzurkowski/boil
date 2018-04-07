import jinja2

from boil.common import filters


class Environment(jinja2.Environment):

    def __init__(self, plate, **kwargs):
        self.plate = plate
        super(Environment, self).__init__(
            loader=jinja2.PackageLoader(plate.name),
            keep_trailing_newline=True, **kwargs)
        self._setup_filters()

    def _setup_filters(self):
        self.filters.update(filters.PLATE_COMMON_FILTERS)
        self.filters.update(self.plate.filters)
