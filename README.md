[travis]: https://travis-ci.org/bzurkowski/boil
[codeclimate]: https://codeclimate.com/github/bzurkowski/boil/maintainability

# Boil

[![Build Status](https://travis-ci.org/bzurkowski/boil.svg?branch=master)][travis]
[![Code Climate](https://api.codeclimate.com/v1/badges/b56e0c5a0856da0c35ba/maintainability)][codeclimate]

## Installation

Use pip or easy_install:

```bash
$ pip install boil
```

## Usage

```
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

Initialize new project:

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
