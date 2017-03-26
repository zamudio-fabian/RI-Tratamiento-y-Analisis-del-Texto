#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.Regla import *

class TranslateRegla(Regla):
 
    content = ""

    def __init__(self,content):
        self.content = content
        
    def run(self):
        content = self.translate(self.content)
        return content

    def translate(self,to_translate):
        tabin = u'áéíóúñ'
        tabout = u'aeioun'
        tabin = [ord(char) for char in tabin]
        translate_table = dict(zip(tabin, tabout))
        return to_translate.translate(translate_table).encode('utf-8')
        