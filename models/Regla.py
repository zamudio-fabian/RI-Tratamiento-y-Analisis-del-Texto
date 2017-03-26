#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Regla:

    tokens = []

    def __init__(self,tokens):
        self.tokens = tokens
        
    def run(self):
        sys.exit(-1)