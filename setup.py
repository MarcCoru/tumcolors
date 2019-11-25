import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tumcolors",
    version = "0.0.1",
    author = "Marc Rußwurm",
    author_email = "marc.russwurm@tum.de",
    description = ("A utility package to import tumcolors"),
    license = "BSD",
    install_requires=[
          'numpy',
      ],
    packages=['tumcolors'],
)
