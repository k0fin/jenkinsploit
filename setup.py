#!/usr/bin/python3

import glob
import os

from setuptools import setup

setup(
    name = "jenkinsploit",
    version = "0.0.1",
    author = "Kory Findley (@k0fin)",
    author_email = None,
    description = ("jenkinsploit"),
    license = "BSD",
    keywords = "jenkins exploit jenkinsploit attack hudson payload",
    url = "https://www.github.com/k0fin/jenkinsploit",
    packages=['scripts', 'modules'],
    scripts = ['scripts/jenkinsploit','scripts/jsfconsole'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
