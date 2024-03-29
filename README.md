# Boil

[![Maintainability](https://api.codeclimate.com/v1/badges/b56e0c5a0856da0c35ba/maintainability)](https://codeclimate.com/github/bzurkowski/boil/maintainability)
[![Package version](https://img.shields.io/pypi/v/boil.svg)](https://pypi.python.org/pypi/boil)
[![License](https://img.shields.io/pypi/l/boil.svg)](https://pypi.python.org/pypi/boil)
[![Python versions](https://img.shields.io/pypi/pyversions/boil.svg)](https://pypi.python.org/pypi/boil)
[![Coverage](https://img.shields.io/codecov/c/github/bzurkowski/boil.svg)](https://codecov.io/gh/bzurkowski/boil)

------------------------------------------------------------------------

**Initialization of new software projects should be quick and easy.
Period.**

Boil aims to build a centralized, pluggable and community-driven
repository of project templates for various technologies, managed via
single API.

These are the problems that it aims to solve:

-   **Wasting time on initializing new software projects from scratch**

    In particular: creating a file structure, checking naming
    conventions, determining dependencies and completing basic metadata.

-   **Poor quality and lack of consistency between projects**

    Most developers initiate projects in their own way without complying
    with generally accepted standards. Often due to lack of time,
    projects are initialized neglectfully, have no maintenance-friendly
    structure and are poorly documented.

-   **Burden of bootstrapping tools**

    Separate app generator for Ansible, Django, or Rails. Switching
    between one and the other may be troublesome considering the variety
    of APIs and different configuration options for each tool.

## Installation

Use pip or easy_install:

    $ pip install boil

## Usage

    $ boil
    Usage:
        boil list
        boil search <phrase>
        boil new <plate_name> [--target-dir=<dir>]
        boil -h | --help

    Options:
        --target-dir=<dir>  Target directory where project files should be
                            populated.

List all available plates:

    $ boil list

Search for plates:

    $ boil search <phrase>

Initialize new project from selected plate:

    $ boil new <plate_name>

### Examples

List all available plates:

    $ boil list

Search for Python-related plates:

    $ boil search python

Initialize new Python package:

    $ boil new python_package

Initialize new Django app:

    $ boil new django_app

Initialize new Rails app:

    $ boil new rails_app

Initialize new Ruby gem:

    $ boil new gem

Initialize new Bash command-line tool:

    $ boil new bash_cli

Initialize new Ansible role:

    $ boil new ansible_role

Initialize new plate:

    $ boil new plate

## Changelog

All notable changes to this project are documented in the [CHANGELOG](CHANGELOG.rst).
