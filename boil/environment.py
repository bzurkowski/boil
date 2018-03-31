from jinja2 import Environment, PackageLoader

from boil import filters


def get_environment(plate):
    env = Environment(
        loader=PackageLoader(plate.__name__))
    env.filters.update(filters.TEMPLATE_FILTERS)
    return env
