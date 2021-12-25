from setuptools import setup, find_packages

setup(
    name='mb',
    version='1.0.0',
    description='Use advanced impulse techniques to soothe and de-stress your terminal.',
    url='https://github.com/catern/mb',
    author='catern',
    author_email='sbaugh@catern.com',
    license='MIT',
    packages=['mb'],
    entry_points={
        'console_scripts': ['mb=mb.main:main'],
    },
)
