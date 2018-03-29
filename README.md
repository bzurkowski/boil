# Boil

## Installation

Use pip or easy_install:

```bash
$ pip install boil
```

## Usage

Search for available application boilerplates:

```bash
$ boil search [APP_NAME]
```

Examples:

```bash
# Search for available Python-related boilerplates
$ boil search python
python-package python-script django-app flask-app flask-api
```

Initialize new application:

```bash
$ boil new [APP_NAME]
```

Examples:

```bash
# New Python package
$ boil new python-package

# New Django app
$ boil new django-app

# New Rails 5 app
$ boil new rails-app --version 5.1

# New Ruby gem
$ boil new gem

# New Ansible role
$ boil new ansible-role

# New boilerplate
$ boil new boilerplate
```
