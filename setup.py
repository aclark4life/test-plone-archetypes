from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
        'z3c.autoinclude.plugin': 'target=plone',
    },
    name='at_test',
    packages=find_packages(),
)
