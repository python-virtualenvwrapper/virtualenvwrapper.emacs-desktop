#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Control emacs desktop-mode when changing virtual environments.
"""

import logging
import os
import subprocess

log = logging.getLogger(__name__)

def post_activate(args):
    """Change the location of the desktop file to the new environment.
    """
    if not os.environ.get('DESKTOP_CONTROLLER'):
        return
    lisp = '(desktop-change-dir "%s")' % os.environ['VIRTUAL_ENV']
    log.debug(lisp)
    # It would be simpler to use subprocess.call(), but then
    # every time we run emacsclient the 't' result is printed
    # to the console.  Setting up the pipe and then not doing
    # anything with the output prevents the noise.
    cmd = subprocess.Popen(['emacsclient', '-e', lisp], stdout=subprocess.PIPE)
    cmd.communicate()
    return
