#!/usr/bin/env python3

import os
import sys

import setuptools


def _read_reqs(relpath):
    abspath = os.path.join(os.path.dirname(__file__), relpath)
    with open(abspath) as f:
        return [
            s.strip() for s in f.readlines()
            if s.strip() and not s.strip().startswith('#')
        ]


def _importlib_needs_backport() -> bool:
    major, minor = int(sys.version[0]), int(sys.version[2])
    return major < 3 or major == 3 and minor < 7


_INSTALL_REQUIRES = _read_reqs('requirements.txt') \
                    + ['importlib_resources'] if _importlib_needs_backport() else []

setuptools.setup(
    name='shifaa',
    version='0.0.1',
    install_requires=_INSTALL_REQUIRES,
    tests_require=_read_reqs('tests-requirements.txt'),
    extras_require={
        'dev': _read_reqs('dev-requirements.txt'),
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
)
