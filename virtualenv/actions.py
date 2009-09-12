#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Maybe License
#
# Rıdvan Örsvuran <flasherdn@gmail.com>


from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules



def install():
    pythonmodules.install()
    pisitools.dodoc("docs/index.txt",
                    "docs/license.txt")
