import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pommons",
    version = "0.1",
    author = "Adam Matan",
    author_email = "adam@matan.name",
    description = ("Some convenient Python boilerplates"),
    license = "GPLv3",
    keywords = "Python commons",
    url = "https://github.com/adamatan/pommons",
    packages=['runner',],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
