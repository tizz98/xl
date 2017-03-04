#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


from xl import __str_version__, __author__


setup(
    name='xl',
    version=__str_version__,
    description='A nice way of generating excel formulas in python.',
    long_description=long_description,
    url='https://github.com/tizz98/xl',
    download_url='https://github.com/tizz98/xl/tarball/%s' % (
        __str_version__
    ),
    author=__author__,
    author_email='elijah@elijahwilson.me',
    license='MIT',
    packages=['xl'],
    keywords='xl excel formulas formula formulae',
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
