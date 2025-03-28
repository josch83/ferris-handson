# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "jsctzi_api"
VERSION = "1.0.0"
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
    description="ferris.ai None jsctzi",
    author_email="info@ferris.ai",
    url="",
    keywords=["Swagger", "ferris.ai None jsctzi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['jsctzi_api=jsctzi_api.__main__:main']},
    long_description="""\
    API definition for ferris.ai None jsctzi
    """
)
