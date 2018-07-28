Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog`_
and this project adheres to `Semantic Versioning`_.

.. _Keep a Changelog: https://keepachangelog.com/en/1.0.0/
.. _Semantic Versioning: https://semver.org/spec/v2.0.0.html

Unreleased_
------------

Added
/////
- Python 3 support
- Exclude plate templates from gitignore: restore missing files from Ruby gem plate
- Plate for plate

0.2.0_ - 2018-07-21
--------------------

Added
/////
- Ruby gem plate
- License plate (MIT, Apache 2.0, GNU)
- Excluding template paths by regex
- setup.py command to build and publish the package

Changed
///////
- Python plate: added testing environment
- Python plate: added exceptions base
- Enabled trimming Jinja blocks in template environment 

0.1.5 - 2018-05-13
--------------------

Added
/////
- Foundations of plates framework
- Python package plate
- Python script plate
- Ansible role plate
- Bash script plate

.. _Unreleased: https://github.com/bzurkowski/boil/compare/v0.2.0...HEAD
.. _0.2.0: https://github.com/bzurkowski/boil/compare/v0.1.5...v0.2.0