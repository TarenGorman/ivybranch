from setuptools import setup, find_packages

setup(
    name='ivybranch',
    version='v0.1',
    dependencies=[p.split("\n")[0] for p in open("./requirements.txt")],
    packages=find_packages(),
    license='MIT',
)