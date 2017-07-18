#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

PYVERSION = sys.version.split()[0]

if PYVERSION >= "3" or PYVERSION < "2.6":
    exit("[CRITICAL] incompatible Python version detected ('%s'). For successfully running Maltrail you'll have to use version 2.6 or 2.7 (visit 'http://www.python.org/download/')" % PYVERSION)
