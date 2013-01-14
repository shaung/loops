# -*- coding: utf-8 -*-

__VERSION__ = '0.0.1'

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

params = {
    'name': 'loop',
    'version': __VERSION__,
    'description': '',
    'long_description': read('README.md'),
    'author': 'shaung',
    'author_email': 'shaun.geng@gmail.com',
    'url': 'https://github.com/shaung/loop/',
    'py_modules': ['loop'],
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
