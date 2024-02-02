from setuptools import setup, find_packages

setup(
    name="is_bigger",
    packages=find_packages(include=["is_bigger"]),
    version="0.1.1",
    description="A package to compare two integers",
    author="ShackledMars261",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)