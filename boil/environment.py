from jinja2 import Environment, PackageLoader, select_autoescape


def get_environment(plate_name):
    plate_package = 'boil.plates.%s' % plate_name
    return Environment(
        loader=PackageLoader(plate_package))
