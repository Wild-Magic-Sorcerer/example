#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='example',
    version='0.0.1',
    packages=find_packages("."),
    scripts=["bin/example"],
    url='https://gitlab.com/Wild_Magic_Sorcerer/example/',
    license='Apache-2.0',
    author='Sergey Gorelov',
    author_email='Infinity2573@gmail.com',
    description='Example module for display and observation.',
    include_package_data=True,
    install_requires=[
        "setuptools",
        "numpy",
        "matplotlib"
      ],
)
