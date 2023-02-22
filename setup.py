import os
import sys
from shutil import rmtree

from setuptools import setup, find_packages, Command


base_dir = os.path.abspath(os.path.dirname(__file__))

pkg_metadata = {}
with open(os.path.join(base_dir, "boil", "__version__.py")) as f:
    exec(f.read(), pkg_metadata)


def get_description():
    with open("README.md") as readme:
        return readme.read()


def get_requirements():
    with open("requirements.txt") as requirements:
        return requirements.read().splitlines()


class UploadCommand(Command):

    """Extends setup.py with a command to build and publish the package."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(base_dir, "dist"))
        except OSError:
            pass
        self.status("Building Source distribution...")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPi via Twine...")
        os.system("twine upload dist/*")
        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(pkg_metadata["__version__"]))
        os.system("git push --tags")
        sys.exit()


setup(
    name="boil",
    version=pkg_metadata["__version__"],
    description="Radically simple app initialization",
    long_description_content_type="text/markdown",
    long_description=get_description(),
    url="https://github.com/bzurkowski/boil",
    author="Bartosz Zurkowski",
    license="MIT",
    install_requires=get_requirements(),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "boil = boil.cli:main",
        ],
        "boil.plates": [
            "python_package = boil.plates.python_package",
            "ansible_role = boil.plates.ansible_role",
            "bash_script = boil.plates.bash_script",
            "license = boil.plates.license",
            "ruby_gem = boil.plates.ruby_gem",
            "plate = boil.plates.plate",
        ],
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    include_package_data=True,
    zip_safe=False,
    cmdclass={"upload": UploadCommand},
)
