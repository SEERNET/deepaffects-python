# coding: utf-8


from setuptools import setup, find_packages
from pypandoc import convert

NAME = "deepaffects"
VERSION = "1.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "pymediainfo >= 2.1.9"]

def readme():
    return convert('README.md', 'rst')

setup(
    name=NAME,
    version=VERSION,
    description="Python bindings for DeepAffects APIs",
    author_email="support@seernet.io",
    url="https://github.com/SEERNET/deepaffects-python",
    author="Sushant Hiray, Venkatesh Duppada",
    setup_requires=[
        "six >= 1.3.0",
        "pillow >= 2.8.1"
    ],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=readme()
)
