#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Termino:

    CF = 0
    DOCS = []
    label = ""

    def __init__(self,label,CF,DOC):
        self.label = label
        self.CF = CF
        self.DOCS.append(DOC)

    def addCf(self):
        self.CF += 1

    def addDoc(self,doc):
        if doc not in self.DOCS :
            self.DOCS.append(doc)