#!/usr/bin/python

from distutils.core import setup

setup(name='pyfern',
    version='1.0',
    description='Generate SVGs for Barnsley fern-like fractals',
    author='Mario Holldack',
    author_email='mario@holldack.org',
    install_requires=["svgwrite"]
)
