# coding: utf-8


import sys
from setuptools import setup, find_packages

NAME = "deepaffects"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="DeepAffects APIs",
    long_description=long_description,
    author_email="engineering@seernet.io",
    url="https://github.com/SEERNET/deepaffects-python",
    author="Sushant Hiray, Venkatesh Duppada",
    setup_requires=[
        "six >= 1.3.0",
        "pillow >= 2.8.1"
    ],
    install_requires=REQUIRES,
    packages=find_packages(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Audio Analysis",
        "Topic :: Scientific/Engineering :: Text Analysis",
        "Topic :: Scientific/Engineering :: Emotion Analysis",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    include_package_data=True
)
