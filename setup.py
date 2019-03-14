#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='pylepton',
      version='0.1.2',
      description='FLIR Lepton interface library for Python',
      author='Kurt Kiefer',
      author_email='kurt@kieferware.com',
      url='https://github.com/kekiefer/pylepton',
      packages = find_packages('.'),
      scripts = ["pylepton_capture", "pylepton_overlay"],
      install_requires = ['numpy', 'opencv-contrib-python'],
     )
