#-*- coding:utf-8 -*-
#
# Copyright (C) 2008 - Olivier Lauzanne <olauzanne@gmail.com>
# Copyright (C) 2011 - David Schoonover <david.schoonover@gmail.com>
#
# Distributed under the BSD license, see LICENSE.txt

from setuptools import setup, find_packages
import sys, os

def read(*names):
    values = dict()
    for name in names:
        filename = name+'.txt'
        if os.path.isfile(filename):
            value = open(name+'.txt').read()
        else:
            value = ''
        values[name] = value
    return values

long_description="""
%(README)s

See http://packages.python.org/pyquery/ for the full documentation

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

version = '1.1'

setup(name='pyquery',
      version=version,
      description='A jQuery-like library for Python',
      long_description=long_description,
      classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        ],
      keywords='jquery html xml',
      maintainer='David Schoonover',
      maintainer_email='dsc@less.ly',
      author='Olivier Lauzanne',
      author_email='olauzanne@gmail.com',
      url='https://github.com/dsc/pyquery',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lxml>=2.1'
      ],
      test_requires=['nose'],
      test_suite='nose.collector',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
