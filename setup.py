# -*- coding: utf-8 -*-
from distutils.core import setup

from setuptools import find_packages


def get_version():
    return '0.2.0'


def get_requirements():
    with open('requirements.txt', 'rU') as fhan:
        requires = [line.strip() for line in fhan.readlines()]
    return requires


def get_long_description():
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')

        readme_note = """\
        .. note::
           For the latest source, discussion, etc, please visit the
           `GitHub repository <https://github.com/shubhamchaudhary/qmon>`_\n\n"""
        long_description = readme_note + long_description
        with open('README.rst', 'w') as fhan:
            fhan.write(long_description)
    except (IOError, ImportError) as e:
        raise e
        with open('README.md') as fhan:
            long_description = fhan.read()
    return long_description


if __name__ == '__main__':
    add_keywords = dict(
        entry_points={
            'console_scripts': ['qmon = qmon.main:main'],
        }, )

    setup(
        name='QMon',
        description='Redis Monitor - monitor number of items and more for any type of redis queue',
        version=get_version(),
        packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/qmon',
        long_description=get_long_description(),
        install_requires=get_requirements(),
        **add_keywords)
