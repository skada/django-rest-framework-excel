#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from setuptools import setup
import re
import os
import sys


name = 'djangorestframework-excel'
package = 'rest_framework_excel'
description = 'Excel Render for Django REST Framework'
url = 'https://github.com/diegueus9/django-rest-framework-excel'
author = 'Diego Andres Sanabria'
author_email = 'diegueus9@gmail.com'
license = 'Apache'
install_requires = ['djangorestframework', 'openpyxl', 'ordereddict', 'six']


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]
    print([x for x in os.walk(package)])
    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    print(package, filepaths)
    return {package: filepaths}


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data={},
    install_requires=install_requires,
    # classifiers=[
    #     "Development Status :: 4 - Beta",
    #     "Environment :: Web Environment",
    #     "Intended Audience :: Developers",
    #     "License :: OSI Approved :: Apache Software License",
    #     "Operating System :: OS Independent",
    #     "Programming Language :: Python",
    #     "Programming Language :: Python :: 2",
    #     "Programming Language :: Python :: 2.6",
    #     "Programming Language :: Python :: 2.7",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.2",
    #     "Programming Language :: Python :: 3.3",
    #     "Programming Language :: Python :: 3.4",
    #     "Programming Language :: Python :: 3.5",
    #     "Programming Language :: Python :: 3.6",
    #     # "Framework :: Django",
    # ],
)
