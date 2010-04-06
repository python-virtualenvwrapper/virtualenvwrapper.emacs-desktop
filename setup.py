#!/usr/bin/env python

PROJECT = 'virtualenvwrapper-emacs-desktop'
VERSION = '1.0'

# Bootstrap installation of Distribute
import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

import os
import sys

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name = PROJECT,
    version = VERSION,
    
    description = 'virtualenvwrapper plugin to control emacs desktop mode',
    long_description = long_description,
    
    author = 'Doug Hellmann',
    author_email = 'doug.hellmann@gmail.com',

    url = 'http://www.doughellmann.com/projects/%s/' % PROJECT,
    download_url = 'http://www.doughellmann.com/downloads/%s-%s.tar.gz' % \
                    (PROJECT, VERSION),

    classifiers = [ 'Development Status :: 5 - Production/Stable',
                    'License :: OSI Approved :: BSD License',
                    'Programming Language :: Python',
                    'Intended Audience :: Developers',
                    'Environment :: Console',
                    ],

    platforms = ('Any',),

    provides=['virtualenvwrapper.emacs_desktop',
              ],
    requires=['virtualenv',
              'virtualenvwrapper (>=2.0)',
              ],

    namespace_packages = [ 'virtualenvwrapper' ],
    packages = find_packages(),
    include_package_data = True,

    entry_points = {
        'virtualenvwrapper.initialize_source': [
            'user_scripts = virtualenvwrapper.emacs_desktop:initialize_source',
            ],
        'virtualenvwrapper.post_activate': [
            'user_scripts = virtualenvwrapper.emacs_desktop:post_activate',
            ],
        },

    zip_safe=False,
    )
