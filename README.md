[travis]: https://travis-ci.org/bzurkowski/boil
[codeclimate]: https://codeclimate.com/github/bzurkowski/boil/maintainability

# Boil

[![Build Status](https://travis-ci.org/bzurkowski/boil.svg?branch=master)][travis]
[![Code Climate](https://api.codeclimate.com/v1/badges/b56e0c5a0856da0c35ba/maintainability)][codeclimate]

**Initialization of new software projects should be quick and easy.**

Boil tries to solve the following problems:

* Wasting time on the initialisation of new software projects from scratch: creating a file structure, thinking about naming conventions, researching best practices - almost always requires documentation lookup.

* No consistency between projects. Everyone initiates projects in their own way, often in an incorrect way.

* Burden of bootstrapping tools for different technologies (separate app generator for Ansible, Django, Flask, etc.).

* Lack of boilerplates for many software categories. If they already exist, they require reading through the documentation to find out how to use them.

Here is how:

* Use the [Jinja](http://jinja.pocoo.org/) templating engine to dynamically generate project files. Ask the user for a minimal set of variables (such as project name, author, license etc.) and inject them into the right place.

* Organize a centralized, plugable repository for project templates. Let the community decide on their final form.

* Provide a single API for initializing projects in any technology.

## Installation

Use pip or easy_install:

```bash
$ pip install boil
```

## Usage

```
$ boil
Usage:
  boil new <plate_name>
  boil list
  boil search <phrase>
```

List available plates:

```
$ boil list
```

Search for plates:

```
$ boil search <phrase>
```

Initialize new project from plate:

```
$ boil new <plate_name>
```

#### Examples

```bash
# List available plates
$ boil list
Available plates:
python_package
python_script
...

# Search for Python-related plates:
$ boil search python
Found plates:
python_package
python_script
...

# Initialize new Python package
$ boil new python-package

# Initialize new Django app
$ boil new django-app

# Initialize new Rails 5 app
$ boil new rails-app

# Initialize new Ruby gem
$ boil new gem

# Initialize new Ansible role
$ boil new ansible-role

# Initialize new plate
$ boil new plate
```
