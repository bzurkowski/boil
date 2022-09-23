import jinja2

from boil.common import filters


class Environment(jinja2.Environment):
    def __init__(self, package_name):
        loader = jinja2.PackageLoader(package_name)
        super(Environment, self).__init__(
            loader=loader,
            keep_trailing_newline=True,
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self._setup_filters()

    def _setup_filters(self):
        self.filters.update(filters.TEMPLATE_FILTERS.copy())
