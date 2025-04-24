# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "magdemo_api"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="ferris.ai Ferris Demo Project for MAG Hands On",
    author_email="info@ferris.ai",
    url="",
    keywords=["Swagger", "ferris.ai Ferris Demo Project for MAG Hands On"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['magdemo_api=magdemo_api.__main__:main']},
    long_description="""\
    API definition for ferris.ai Ferris Demo Project for MAG Hands On
    """
)
