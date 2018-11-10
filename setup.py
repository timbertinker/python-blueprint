#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='python-blueprint',
    version='1.0.0',

    description='Example Python project',
    long_description=open('README.rst').read(),
    keywords=('python',),

    author='John Hagen',
    url='https://github.com/johnthagen/python-blueprint',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
