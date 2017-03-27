#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from models.Regla import *

class AbreviaturasRegla(Regla):

    def __init__(self,content):
        pass
        
    def run(self,content):
        # Eliminamos tags básicos de ej: <img ... />
        content = re.sub(u"<(.|\n)*?>", "", content)
        # # Eliminamos entities de HTML ej: &quote;
        content = re.sub(u"&[a-z]*;", "", content)
        return content