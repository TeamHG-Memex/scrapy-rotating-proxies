#!/usr/bin/env python
from setuptools import setup, find_packages
import re
import os
import sys


def get_version():
    fn = os.path.join(os.path.dirname(__file__), "rotating_proxies", "__init__.py")
    with open(fn) as f:
        return re.findall("__version__ = '([\d.\w]+)'", f.read())[0]


def get_long_description():
    readme = open('README.rst').read()
    changelog = open('CHANGES.rst').read()
    return "\n\n".join([
        readme,
        changelog.replace(':func:', '').replace(':ref:', '')
    ])


# Do not install typing on python 3.7+
INSTALL_REQUIRES = [
    'attrs > 16.0.0',
    'six',
]
if sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] <= 6):
    INSTALL_REQUIRES.append("typing")


setup(
    name='scrapy-rotating-proxies',
    version=get_version(),
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',
    license='MIT license',
    long_description=get_long_description(),
    description="Rotating proxies for Scrapy",
    url='https://github.com/TeamHG-Memex/scrapy-rotating-proxies',
    packages=find_packages(exclude=['tests']),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Scrapy',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
