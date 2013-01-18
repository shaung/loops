# -*- coding: utf-8 -*-

__VERSION__ = '0.0.1'

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

params = {
    'name': 'loops',
    'version': __VERSION__,
    'description': 'Loop context utility inspired by Mako',
    'long_description': read('README.md'),
    'author': 'shaung',
    'author_email': 'shaun.geng@gmail.com',
    'url': 'https://github.com/shaung/loops/',
    'py_modules': ['loops'],
    'license': 'BSD',
    'download_url': '',
    'zip_safe': False,
    'classifiers': [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
}

from setuptools import setup
setup(**params)
