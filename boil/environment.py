from jinja2 import Environment, PackageLoader

from boil import filters


def get(plate_module):
    env = Environment(
        loader=PackageLoader(plate_module.__name__),
        keep_trailing_newline=True)
    env.filters.update(filters.TEMPLATE_FILTERS)
    return env
