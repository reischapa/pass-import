#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

VERSION = '2.3'
URL = 'https://github.com/roddhjav/pass-import'

setup(
    name="pass-import",
    version=VERSION,
    author="Alexandre Pujol",
    author_email="alexandre@pujol.io",
    url=URL,
    download_url="%s/releases/download/v%s/pass-import-%s.tar.gz"
                 % (URL, VERSION, VERSION),
    description="A pass extension for importing data from most of the existing password manager.",
    license='GPL3',

    py_modules=["lib/import"],
    data_files=[
        ('lib/password-store/extensions', ['import.bash']),
        ('share/man/man1/', ['pass-import.1']),
        ('share/doc/pass-import', ['README.md', 'CHANGELOG.md']),
        ],

    install_requires=[
        'defusedxml'
        ],
    setup_requires=[
        'green'
        ],
    test_suite='tests',
    python_requires='>=3.4',

    keywords=[
        'password-store', 'password', 'pass', 'pass-extension',
        'password-manager', 'importer',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security :: Cryptography',
        ],
)