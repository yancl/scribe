#!/usr/bin/env python
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r internal')
    sys.exit()

setup(
        name = "scribe_client",
        version = "0.12",
        description="python scribe client for facebook scribed",
        long_description=open("README.md").read(),
        author="yancl",
        author_email="kmoving@gmail.com",
        url='https://github.com/yancl/scribe_client',
        classifiers=[
            'Programming Language :: Python',
        ],
        platforms='Linux',
        license='MIT License',
        zip_safe=False,
        install_requires=[
            'distribute',
            'thrift_client',
            'scribe',
        ],
        tests_require=[
            'nose',
        ],
        packages=['scribe_client']
)
