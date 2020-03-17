#!/usr/bin/env python3

"""Setup this Python package."""

from distutils.core import setup

from setuptools import find_packages


def _read_file(f):
    return open(f).read().split("\n")


VERSION = _read_file("VERSION")[0]
REQUIREMENTS = _read_file("requirements.txt")

setup(
    name="dygma",
    version=VERSION,
    description="An API interface to the Dygma keyboard",
    author="Brandon Chinn",
    author_email="brandonchinn178@gmail.com",
    url="https://github.com/brandonchinn178/dygma-api",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["dygma = dygma.cli:main"]},
)
