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

from glob import glob
import logging
import subprocess

class Software:
    def __init__(self):
        pass

    def listPackages(self):
        return glob("software/*")

    def installPackages(self, pkglist):
        for pkg in pkglist:
            with open(pkg) as f:
                apps = f.readlines()
                cmds = []
                buff = apps[:]

                for entry in buff:
                    if(entry[:3] == '$: '):
                        apps.remove(entry)
                        cmds.append("".join(entry).replace('\n', '').replace('$: ', ''))
                    elif(entry[:3] == '#: '):
                        apps.remove(entry)
                        pkgname = "software/" + "".join(entry).replace('\n', '').replace('#: ', '')
                        pkglist.append(pkgname)

                applications = " ".join(apps).replace('\n', '')
                logging.info("Installing Extra Packages: \'{}\'".format(applications))
                logging.info("Invoking subprocess arch-chroot /mnt pacman")
                p = subprocess.Popen(["arch-chroot", "/mnt", "pacman", "--noconfirm", "-S"] + applications.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                for line in p.stdout:
                    l = line.decode("utf-8")
                    logging.debug("STDOUT: " + l )
                    yield l

                p.wait()
                logging.info("Process exited with code " + str(p.returncode))

                for cmd in cmds:
                    logging.info("Invoking command in chroot: {}".format(cmd))
                    pc = subprocess.Popen(["arch-chroot", "/mnt"] + cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    for line in pc.stdout:
                        l = line.decode("utf-8")
                        logging.debug("STDOUT: " + l )
                        yield l

                    pc.wait()
                    logging.info("Process exited with code " + str(pc.returncode))
