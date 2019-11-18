import setuptools as s

s.setup(
    name='ivybranch',
    version='v0.1',
    dependencies=[p.split("\n")[0] for p in open("./requirements.txt")],
    packages=["ivybranch"],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)