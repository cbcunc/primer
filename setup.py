#! /usr/bin/env python

"""Setup script for the primer package."""

from setuptools import setup
from setuptools import find_packages

__version__ = "1.0.2"


def long_description():
    with open("README.rst") as r:
        l1 = r.read()
    with open("HISTORY.txt") as h:
        l2 = h.read()
    return "\n".join([l1, l2, ])


setup(name="primer",
      version=__version__,
      license="GPL2",
      packages=find_packages(),
      author="Chris Calloway",
      author_email="cbc@chriscalloway.org",
      description="A primer for prime numbers",
      long_description=long_description(),
      url="https://github.com/cbcunc/primer",
      keywords="Prime number primes primorial",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: "
                   "GNU General Public License v2 (GPLv2)",
                   "Topic :: Scientific/Engineering :: Mathematics",
                   ],
      zip_safe=False,
      test_suite="primer.tests")
