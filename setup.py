#! /usr/bin/env python

"""Setup script for the primer package."""

from setuptools import setup
from setuptools import find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='primer',
      version='1.0',
      license="GPL2",
      packages=find_packages(),
      author='Chris Calloway',
      author_email='cbc@chriscalloway.org',
      description='A primer for prime numbers',
      long_description=readme(),
      url="https://github.com/cbcunc/primer",
      keywords="Prime number primes primordial",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: "
                   "GNU General Public License v2 (GPLv2)",
                   "Topic :: Scientific/Engineering :: Mathematics",
                   ],
      zip_safe=False,
      test_suite="primer.tests")
