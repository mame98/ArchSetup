#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of ArchSetup.
#
# ArchSetup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArchSetup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArchSetup.  If not, see <http://www.gnu.org/licenses/>.

from SetupTools.Locale import Locale
import logging


class SetupConfig:
    def __init__(self):
        self.locales = []

    def logChange(self, key, value):
        logging.info("Changed Setup parameter \'{}\' to \'{}\'".format(key, value))

    def setkeyboard(self, layout):
        self.logChange("keyboardlayout", layout)
        self.keyboard = layout

    def setfont(self, font):
        self.logChange("console.font", font)
        self.font = font

    def gettimezone(self):
        return self.timezone

    def settimezone(self, zone):
        self.logChange("time.zone", zone)
        self.timezone = zone

    def settimesubzone(self, subzone):
        self.logChange("time.subzone", subzone)
        self.timesubzone = subzone

    def sethostname(self, hostname):
        self.logChange("hostname", hostname)
        self.hostname = hostname

    def setdisk(self, disk):
        self.logChange("disk.device", disk)
        self.disk = disk

    def setrootpassword(self, key):
        self.logChange("user.root.key", '<hidden>')
        self.rootpassword = key

    def setuserdata(self, username, homedir, realname, passwd):
        self.logChange("user.username", username)
        self.logChange("user.homedir", homedir)
        self.logChange("user.realname", realname)
        self.logChange("user.passwd", "<hidden>")
        self.username = username
        self.homedir = homedir
        self.realname = realname
        self.password = passwd

    def setnetwork(self, net):
        self.logChange("network.type", net)
        self.network = net

    def setfilesystem(self, fs):
        self.logChange("filesystem.type", fs)
        self.filesystem = fs

    def setlocales(self, locales):
        self.logChange("locales", locales)
        self.locales = locales

    def getlocales(self):
        if(len(self.locales) > 0):
            return self.locales
        else:
            temp = Locale()
            return temp.list_locales() # This should avoid crashes

    def setmainlocale(self, mainlocale):
        self.logChange("locales.main", mainlocale)
        self.mainlocale = mainlocale

    def setsoftware(self, software):
        self.logChange("software", software)
        self.software = software

    def getnetwork(self):
        return self.network
