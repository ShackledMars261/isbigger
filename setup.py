from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="is_bigger",
    packages=find_packages(include=["is_bigger"]),
    version="0.1.9",
    description="A package to compare two integers",
    author="ShackledMars261",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)