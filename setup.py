import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "evecentral",
    version = "0.0.1",
    author = "Tyler Dixon",
    author_email = "tyler@chlystyk.com",
    description = "A small module to cache eve central prices in memory",
    licence = "BSD",
    keywords = "eve evecentral",
    url = "https://github.com/ZymoticB/python-evecentral",
    packages = ['evecentral'],
    long_description=read('README.rst'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries",
    ],
)
