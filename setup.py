import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="rock_paper_stuff",
    version="0.0.1",
    author="Edward Pantridge",
    description="A python implementation of a game designed by Lee Spector for AI research and education.",
    url="https://github.com/erp12/rock-paper-stuff-python",
    packages=find_packages(exclude=['examples', 'tests*']),
    long_description=read('README.md'),
)
