#!/usr/bin/env python
# -*- coding:utf-8 -*-

from mongoengine import *


class Ninfo(Document):

    ip = StringField(max_length=30, required=True)
    port = IntField(default=0, required=True)
    banner = StringField(max_length=30, required=True)

    @classmethod
    def save(cls, ip, port, banner):
        ni = cls()
        ni.ip = ip
        ni.port = port
        ni.banner = banner
        ni.save()
        return True
