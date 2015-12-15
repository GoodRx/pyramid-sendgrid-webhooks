#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'pyramid>=1.4.0',
]

test_requirements = [
    'pytest',
    'webtest',
]


setup(
    name='pyramid_sendgrid_webhooks',
    version='1.0.0',
    description="Parses incoming Sendgrid Webhooks in Pyramid apps",
    long_description=readme + '\n\n' + history,
    author="Kyle Stark",
    author_email='kyle@goodrx.com',
    url='https://github.com/GoodRx/pyramid-sendgrid-webhooks',
    packages=[
        'pyramid_sendgrid_webhooks',
    ],
    package_dir={'pyramid_sendgrid_webhooks':
                 'pyramid_sendgrid_webhooks'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='pyramid_sendgrid_webhooks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
