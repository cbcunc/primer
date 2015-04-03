#! /usr/bin/env python

"""Setup script for the primer package."""

from setuptools import setup
from setuptools import find_packages


def version():
    """Get the version number."""

    with open("VERSION.txt") as v:
        _version = v.read()
    return _version.strip()


__version__ = version()


def long_description():
    """Construct the long description text."""

    with open("README.rst") as r:
        long_description_1 = r.read()
    with open("HISTORY.txt") as h:
        long_description_2 = h.read()
    return "\n".join([long_description_1, long_description_2, ])


setup(name="primer",
      version=__version__,
      license="GPL2",
      packages=find_packages(),
      author="Chris Calloway",
      author_email="cbc@chriscalloway.org",
      description="A primer for prime numbers",
      long_description=long_description(),
      url="https://github.com/cbcunc/primer",
      download_url="https://github.com/cbcunc/primer/tarball/" + __version__,
      keywords="Prime number primes primorial",
      classifiers=["Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: "
                   "GNU General Public License v2 (GPLv2)",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3.4",
                   "Topic :: Scientific/Engineering :: Mathematics",
                   ],
      zip_safe=False,
      test_suite="primer.tests")
