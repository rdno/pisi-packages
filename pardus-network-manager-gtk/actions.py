#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# license:gpl v3
#
# Rıdvan Örsvuran <flasherdn@gmail.com>


from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pythonmodules.install()
    pisitools.dodoc("README")
    for lang in ["en",  "tr"]:
        pisitools.domo("po/%s.po" % lang, lang, "network_manager_gtk.mo")
    pisitools.rename("/usr/bin/network-manager-gtk.py", "network-manager-gtk")
    #to avoid file conflicts
    pisitools.remove("/usr/lib/python2.6/site-packages/asma/addons/__init__.py")

