#!/bin/bash
DEST=org.cpufreq.scaling_governor
OBJECT=/PowerMode
INTERFACE=set

dbus-send --system --type=method_call --dest=$DEST --print-reply $OBJECT $DEST.$INTERFACE string:$1
