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

**Initialization of new software projects should be quick and easy. Period.**

Boil tries to solve the following problems:

- **Wasting time on initializing new software projects from scratch**

  Creating a file structure, thinking about naming conventions, determining dependencies, completing basic metadata... almost always requires documentation lookup. This time can be usefully spent on something else. For example, making coffee or eating a watermelon!

- **Poor quality and lack of consistency between projects**

  Most developers initiate projects in their own way without complying with generally accepted standards. Often due to lack of time, projects are initialized neglectfully, have no maintenance-friendly structure and are poorly documented.

- **Burden of bootstrapping tools**

  Separate app generator for Ansible, Django, Rails, etc.. Their advantage is greater flexibility and extended functionality, but it is not always what you needed. Switching between one and the other may be troublesome considering the variety of APIs and different configuration options for each tool.

Boil's mission is to build a centralized, pluggable and community-driver repository of project templates for various technologies, managed via single API.

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
