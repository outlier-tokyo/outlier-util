#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pipenv install twine --dev

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'outlier_util'
DESCRIPTION = 'Utils for data analytics, developed by Outlier co. ltd.'
URL = 'https://github.com/outlier-tokyo/outlier-util'
EMAIL = 'info@outlier.tokyo'
AUTHOR = 'Keisuke Nishimura'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name=NAME,
    version=VERSION,
    license="BSD-3-Clause license",
    description=DESCRIPTION,
    author=AUTHOR,
    url=URL,
    packages=find_packages("outlier_util"),
    package_dir={"": "outlier_util"},
    py_modules=[splitext(basename(path))[0] for path in glob('outlier_util/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)