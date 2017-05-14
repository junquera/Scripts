#!/bin/bash
# Remove the dash
dbus-send --session --type=method_call --print-reply --dest=org.gnome.Shell /org/gnome/Shell org.gnome.Shell.Eval string:'Main.overview.connect("showing", function(){Main.overview._dash.actor.hide() })'
# Remove top panel
# dbus-send --session --type=method_call --dest=org.gnome.Shell /org/gnome/Shell org.gnome.Shell.Eval string:'Main.panel.actor.hide();'
