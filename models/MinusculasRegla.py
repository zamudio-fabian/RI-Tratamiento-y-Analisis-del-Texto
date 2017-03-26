#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.Regla import *

class MinusculasRegla(Regla):

    content = ""

    def __init__(self,content):
        self.content = content
        
    def run(self):
        content = self.content.lower();
        return content
        