from jinja2 import Environment, PackageLoader, select_autoescape


def get_environment(plate):
    return Environment(
        loader=PackageLoader(plate.__name__))
