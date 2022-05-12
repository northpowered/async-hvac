#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='async-hvac-fork',
    version='0.6.1',
    description='HashiCorp Vault API client, forked from Aloomaio/async-hvac',
    long_description='HashiCorp Vault API python 3.8+ client using asyncio.',
    author='northpowered',
    author_email='',
    url='https://github.com/northpowered/async-hvac',
    keywords=['hashicorp', 'vault', 'hvac'],
    classifiers=['License :: OSI Approved :: Apache Software License'],
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.1',
    ],
    include_package_data=True,
    package_data={'async_hvac': ['version']},
    extras_require={
        'parser': ['pyhcl==0.3.10']
    }
)
