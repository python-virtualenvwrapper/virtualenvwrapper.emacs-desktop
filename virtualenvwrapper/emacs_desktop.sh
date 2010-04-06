#
# Define functions to enable and disable the plugin by setting
# DESKTOP_CONTROLLER.
#

emacs_desktop_controller_on () {
    export DESKTOP_CONTROLLER="yes"
    echo "Enabling virtualenvwrapper.emacs_desktop"
}

emacs_desktop_controller_off () {
    unset DESKTOP_CONTROLLER
}
