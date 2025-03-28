"""
Setup definition for the distributable package
"""

import importlib.util
import os

from setuptools import find_packages, setup

config = importlib.import_module("config")
version = importlib.import_module(f"{config.FULL_ADDON_NAME}.version")


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname), "r", encoding="utf-8").read()


def desc():
    return read("README.md")


setup(
    name=config.FULL_ADDON_NAME,
    version=version.VERSION_STRING,
    url="/",
    license="BSD",
    author=version.AUTHOR_NAME,
    author_email=version.AUTHOR_EMAIL,
    description=version.DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=desc(),
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    keywords=[
        "package",
        "flask",
    ],
    python_requires=">=3.10",
    install_requires=[
        "Flask-AppBuilder>=4.2.0",
        "jsctzi-api-client==1.0.0",
        "minio>=7.1.13",
    ],
    tests_require=[
        "nose>=1.0",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="nose.collector",
)
