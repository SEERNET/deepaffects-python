# coding: utf-8


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

setup(
    name=NAME,
    version=VERSION,
    description="DeepAffects APIs",
    author_email="engineering@seernet.io",
    url="https://github.com/SEERNET/deepaffects-python",
    author="Sushant Hiray, Venkatesh Duppada",
    setup_requires=[
        "six >= 1.3.0",
        "pillow >= 2.8.1"
    ],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    OpenAPI Specification of DeepAffects APIs
    """
)
