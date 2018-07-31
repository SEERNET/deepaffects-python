# coding: utf-8


from setuptools import setup, find_packages
import os

NAME = "deepaffects"
VERSION = "1.1.8"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "pymediainfo >= 2.1.9", "grpcio==1.13.0",
            "protobuf==3.6.0", "pydub==0.22.1", "pytube==9.2.2"]


def readme():
    try:
        from pypandoc import convert
        return convert('README.md', 'rst')

    except ImportError:
        with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
            return readme.read()

    except OSError:
        with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
            return readme.read()


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
