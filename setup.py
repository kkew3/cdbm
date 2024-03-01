from setuptools import setup

setup(
    name='cdbm',
    packages=['cdbm'],
    package_dir={'': 'src'},
    package_data={'cdbm': ['cdbm.sh', 'help.txt']},
    version='0.2.0',
)
