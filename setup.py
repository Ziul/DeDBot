#!/usr/bin/env python
"""
DBot
===================
A Telegram bot
"""
from setuptools import setup, find_packages

install_requires = [
    'python-telegram-bot>=3.1.2',
    'mock>=1.3.0',
    'PyYAML==3.11',
]

tests_require = ['mock']


setup(
    name="D&DBot",
    version='0.1.0',
    author='Matheus Fernandes, Luiz Oliveira, Lucas Severo',
    author_email='matheus.souza.fernandes@gmail.com, ziuloliveira@gmail.com',
    url='https://github.com/Ziul/DeDBot',
    entry_points={
        'console_scripts': [
            'dice = dice:roll',
            'bot-run = dice:main',
        ]},
    description='A Telegram bot',
    long_description=__doc__,
    license='GPLv3',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3',
        'Topic :: Utilities',
    ],
)
