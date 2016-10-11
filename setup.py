#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
        name='serverfiles',
        description='',
        author='Biolab',
        author_email='marko.toplak@fri.uni-lj.si',
        packages=["serverfiles"],
        install_requires=[
            'requests>=2.11.1',
        ],
        version='0.1',
        zip_safe=False,
        test_suite="tests.suite"
    )
