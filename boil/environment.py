import jinja2

from boil import filters


class PlateEnvironment(jinja2.Environment):

    def __init__(self, plate, **kwargs):
        self.plate = plate
        super(PlateEnvironment, self).__init__(
            loader=jinja2.PackageLoader(plate.__name__),
            keep_trailing_newline=True, **kwargs)
        self._setup_filters()

    def _setup_filters(self):
        self.filters.update(filters.TEMPLATE_FILTERS)


def get(plate, **kwargs):
    return PlateEnvironment(plate, **kwargs)
