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

from SetupTools.Filesystem import Filesystem
from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.SpacerWidget import SpacerWidget
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.ScrollWidget import ScrollWidget
from Interface.Widgets.RadioWidget import RadioWidget

import gettext

class FilesystemWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        self.setupconfig = setupconfig
        self.addwidget(TextWidget(1, 1, _('Please choose a filesystem:'),  40))
        fs = Filesystem()
        buff = fs.list_filesystems()
        if "mkfs.ext4" in buff:
            items = ["mkfs.ext4"]
            buff.remove("mkfs.ext4")
            items += buff
        else:
            items = buff
        self.addwidget(ScrollWidget(3, 1, 40, 20, RadioWidget(0, 0, 40, items, self.event), self.event))
        self.addwidget(SpacerWidget(23, 1, 1))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'refresh':
            self.refresh()
        elif event == 'selection':
            self.setupconfig.setfilesystem(opt)
            pass
        else:
            super().event(event)
