#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from models.Regla import *

class LimpiadoBasicoRegla(Regla):

    content = ""
    def __init__(self,content):
        self.content = content
        
    def run(self):
        content = re.sub(u"[^a-z0-9\s]", "", self.content)
        return content

    