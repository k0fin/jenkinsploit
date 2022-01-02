#!/usr/bin/python3

import glob
import os

from setuptools import setup

setup(
    name = "jenkinsploit-framework",
    version = "0.0.1",
    author = "Kory Findley (k0fin)",
    author_email = None,
    description = ("jenkinsploit-framework"),
    license = "BSD",
    keywords = "jenkins exploit jenkinsploit attack hudson payload",
    url = "https://www.github.com/k0fin/jenkinsploit-framework",
    packages=['scripts', 'modules'],
    scripts = ['scripts/jenkinsploit','scripts/jsfconsole'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
