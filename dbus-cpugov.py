#!/usr/bin/python3
import dbus
import dbus.service
import glob
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop


class DBusDaemon(dbus.service.Object):
    def __init__(self):
        self.bus = dbus.SystemBus()
        bus_name = dbus.service.BusName(
            'org.cpufreq.scaling_governor', bus=self.bus)
        dbus.service.Object.__init__(self, bus_name, '/PowerMode')

    @dbus.service.method('org.cpufreq.scaling_governor', out_signature='b')
    def set(self, mode):
        for cpu_gov in glob.glob('/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'):
            with open(cpu_gov, 'w') as f:
                f.write(mode)
        return True

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    dbus_daemon = DBusDaemon()
    loop = GObject.MainLoop()
    loop.run()
