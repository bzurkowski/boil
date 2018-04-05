Boil
==============================================

.. image:: https://img.shields.io/travis/bzurkowski/boil.svg
    :target: https://travis-ci.org/bzurkowski/boil

.. image:: https://api.codeclimate.com/v1/badges/b56e0c5a0856da0c35ba/maintainability
    :target: https://codeclimate.com/github/bzurkowski/boil/maintainability

.. image:: https://img.shields.io/pypi/v/boil.svg
    :target: https://pypi.python.org/pypi/boil

.. image:: https://img.shields.io/pypi/l/boil.svg
    :target: https://pypi.python.org/pypi/boil

.. image:: https://img.shields.io/pypi/pyversions/boil.svg
    :target: https://pypi.python.org/pypi/boil

---------------

**Initialization of new software projects should be quick and easy.**

Boil tries to solve the following problems:

- Wasting time on the initialisation of new software projects from scratch: creating a file structure, thinking about naming conventions, researching best practices - almost always requires documentation lookup.

- No consistency between projects. Most developers initiate projects in their own way, which is often incorrect or outdated.

- Burden of bootstrapping tools for different technologies (separate app generator for Ansible, Django, Rails, etc.).

- Lack of boilerplates for many software categories. If they already exist, they require manual adjustments.

Here is how:

- Leverage the `Jinja <http://jinja.pocoo.org/>`_ templating engine to automatically generate project files. Ask the user for a minimal set of variables (such as project name, author, license etc.) and inject them into the right place.

- Organize a centralized, plugable repository for project templates. Let the community decide on their final form.

- Provide a single API for initializing projects in any technology.

Installation
------------

Use pip or easy_install::

    $ pip install boil

Usage
-----

::

    $ boil
    Usage:
        boil list
        boil search <phrase>
        boil new <plate_name>
        boil -h | --help

List all available plates::

    $ boil list

Search for plates::

    $ boil search <phrase>

Initialize new project from selected plate::

    $ boil new <plate_name>

Examples
////////

List all available plates::

    $ boil list

Search for Python-related plates::

    $ boil search python

Initialize new Python package::

    $ boil new python_package

Initialize new Django app::

    $ boil new django_app

Initialize new Rails app::

    $ boil new rails_app

Initialize new Ruby gem::

    $ boil new gem

Initialize new Bash command-line tool::

    $ boil new bash_cli

Initialize new Ansible role::

    $ boil new ansible_role

Initialize new plate::

    $ boil new plate
