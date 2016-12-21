#!/usr/bin/env python
from setuptools import setup

setup(
    name='Heutagogy',
    version='1.0',
    url='https://github.com/heutagogy/heutagogy-backend',
    packages=['heutagogy'],
    license='AGPL3',
    install_requires=[
        'Flask',
        'Flask-JWT',
        'Flask-Login',
        'Flask-RESTful',
    ],
)
