#!/usr/bin/env python

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(
    name='Python autoaction',
    version='0.0',
    description='Python Automate Action',
    long_description='',
    author='Yoshiaki Ono',
    author_email='ono.kirin@gmail.com',
    url='',
    download_url='',
    packages=['autoaction'],
    install_requires=[],
)