# -*- coding: utf-8 -*-
from distutils.core import setup
import os

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='tictactui',
    version='0.1',
    python_requires='>3.5.2',
    description='',
    long_description=README,
    author='Harkaitz Agirre Ezama',
    author_email='harkaitz.aguirre@gmail.com',
    url='http://github.com/harkaitz/py-tictactui.git',
    license=LICENSE,
    packages=['tictactui'],
    classifiers=[''],
    entry_points = {
        'console_scripts': [
            'tictactoe = tictactui:tictactoe_main',
        ],
    })
