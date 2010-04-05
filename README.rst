=================================================
 Using Emacs Desktop Mode with Virtualenvwrapper
=================================================

Emacs desktop-mode_ lets you save the state of emacs (open buffers,
kill rings, buffer positions, etc.) between sessions.  It can also be
used as a project file similar to other IDEs.  This virtualenvwrapper_
plugin adds a trigger to save the current desktop file and load a new
one when activating a new virtualenv using ``workon``.

Installation
============

Install this plugin with pip::

  $ pip install virtualenvwrapper-emacs-desktop

Or by unpacking the source distribution and running ``setup.py`` directly::

  $ tar zxvf virtualenvwrapper-emacs-desktop-|release|.tar.gz
  $ cd virtualenvwrapper-emacs-desktop-|relesae|
  $ python setup.py install

You may need administrator privileges to install to a global location.

Configuring Desktop Mode in Emacs
=================================

Setup of desktop-mode is straightforward:

1. Run ``customize-group`` on the "desktop" group.

2. Turn ``desktop-save-mode`` **on** to enable the minor mode.

3. Optionally change the base name for desktop files in
   ``desktop-base-file-name``. For example, using "emacs.desktop"
   means the file will not be hidden.

4. Set a default search path for the desktop file in ``desktop-path``.
   Use your home directory, or the directory where you keep your emacs
   configuration files (``~/emacs.d`` or ``~/emacs``).  This value is
   the *default*.  Your real desktop files will be saved into the
   virtualenv directories.

5. Set ``desktop-save`` to **Always save**. There are other values
   that work, but some require interaction with the editor during the
   context move to confirm file saves.

There are a few other options that may be useful to tweak, depending
on the other features of emacs you use. For example,
``desktop-clear-preserve-buffers`` lets you control which buffers are
saved when the desktop is cleared on a reload.  It may be useful to
save the ``*Messages*``, ``*Org Agenda*``, and ``*scratch*`` buffers,
since those are related to emacs operation and not limited to any one
project.

Enabling the Plugin
===================

Switching desktop sessions every time ``workon`` is used would make it
impossible to have two shells open and working on separate projects at
the same time.  Therefore, before taking any action the plugin
examines the ``DESKTOP_CONTROLLER`` environment variable, looking for
a non-null value.  If the variable is not set, or is defined but
empty, the plugin makes no changes.  If the variable is set to any
value, the session is changed.

Most modern terminal programs make it easy to create custom
configurations with specific settings.  Use your terminal's
customization feature to create a "desktop controller" configuration
with ``DESKTOP_CONTROLLER`` set, then control
virtualenvwrapper-emacs-desktop from a terminal using that
configuration.

References
==========

* `Saving Emacs Sessions <http://www.gnu.org/software/emacs/manual/html_node/emacs/Saving-Emacs-Sessions.html>`__
* `Desktop Save Mode <http://www.gnu.org/s/emacs/manual/html_node/elisp/Desktop-Save-Mode.html>`__
* desktop-mode_
* virtualenvwrapper_

.. _desktop-mode: http://www.emacswiki.org/emacs/DeskTop

.. _virtualenvwrapper: http://www.doughellmann.com/projects/virtualenvwrapper/
