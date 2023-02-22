from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as requirements:
        return requirements.read().splitlines()


setup(
    name="{{ package_name | underscore }}",
    version="0.1.0",
    description="{{ description }}",
    long_description=readme(),
    url="{{ url }}",
    author="{{ author }}",
    license="{{ license }}",
    install_requires=get_requirements(),
    packages=find_packages(),
    zip_safe=False
)
