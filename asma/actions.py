#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# license: gpl v3
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
        pisitools.domo("po/%s.po" % lang, lang, "asma.mo")
    pisitools.rename("/usr/bin/asma.py", "asma")
