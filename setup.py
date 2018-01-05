import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "job-pusher",
    version = "0.0.1",
    author = "Trevor McCasland",
    author_email = "trevormccasland1@gmail.com",
    license = "Apache Software License",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['job-pusher'],
    long_description=read('README.md'),
    classifiers=[
        "Intended Audience :: Information Technology"
        "Intended Audience :: System Administrators"
        "License :: OSI Approved :: Apache Software License",
    ],
)
