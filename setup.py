#!/usr/bin/env python
# -*- coding: utf-8 -*-
import versioneer

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'PyYAML', 'hexdump', 'bitarray', 'argparse'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='mciutil',
    description='MasterCard file utilities',
    long_description=readme + '\n\n' + history,
    author='Anthony Delosa',
    author_email='adelosa@gmail.com',
    url='https://github.com/adelosa/mciutil',
    packages=[
        'mciutil', 'mciutil.cli'
    ],
    include_package_data=True,
    package_data={
        'mciutil.cli': ['*.yml']
    },
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mideu = mciutil.cli.mideu:cli_entry',
            'paramconv = mciutil.cli.paramconv:cli_entry',
        ]
    },
    license='BSD',
    zip_safe=False,
    keywords='mciutil',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
