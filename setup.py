#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup.py file for lupe"""

from setuptools import setup, find_packages

DESCRIPTION = 'Parse command-line arguments made easier'
LONG_DESCRIPTION = open("readme.md").read()

VERSION = '0.0.2'
URL = 'https://projects.abranhe.com/arg'
GITHUB_URL = 'https://github.com/abranhe/arg'

setup(
    name='arg',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    url=URL,
    project_urls={'Source': GITHUB_URL},

    author='Abraham Hernandez',
    author_email='abraham@abranhe.com',
    license='MIT',

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',

        'Operating System :: OS Independent',
        'Operating System :: MacOS',
        'Operating System :: Unix',
    ],

    packages=find_packages(),
    keywords='lib parser args argc',
)
