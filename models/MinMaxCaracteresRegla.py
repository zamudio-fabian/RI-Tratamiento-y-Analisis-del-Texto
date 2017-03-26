#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from models.Regla import *

class MinMaxCaracteresRegla(Regla):

    tokens = ""
    minCarac = 3
    maxCarac = 20

    def __init__(self,tokens):
        self.tokens = tokens
        
    def run(self):
        tokensAux = []
        for token in self.tokens:
            if len(token) >= self.minCarac and len(token) <= self.maxCarac :
                tokensAux.append(token)
        return tokensAux

    