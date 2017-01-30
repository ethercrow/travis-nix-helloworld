#!/usr/bin/env python

from setuptools import setup, find_packages

py_modules = ['lib']

setup(name='travis-nix-helloworld',
      version='1.0',
      packages=find_packages(exclude='ez_setup'),
      py_modules=py_modules,
      install_requires=['six']
     )
