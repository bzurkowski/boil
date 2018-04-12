import jinja2

from boil.common import filters


class Environment(jinja2.Environment):

    def __init__(self, package_name, **kwargs):
        self._set_default_options(kwargs)
        loader = jinja2.PackageLoader(package_name)
        super(Environment, self).__init__(loader=loader, **kwargs)
        self._setup_filters()

    def _set_default_options(self, kwargs):
        kwargs.setdefault('keep_trailing_newline', True)

    def _setup_filters(self):
        self.filters.update(filters.TEMPLATE_FILTERS.copy())
