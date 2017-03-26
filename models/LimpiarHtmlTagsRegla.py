#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from models.Regla import *

class LimpiarHtmlTagsRegla(Regla):

    content = ""

    def __init__(self,content):
        self.content = content
        
    def run(self):
        # Eliminamos tags básicos de ej: <img ... />
        content = re.sub(u"<(.|\n)*?>", "", self.content)
        # # Eliminamos entities de HTML ej: &quote;
        content = re.sub(u"&[a-z]*;", "", content)
        return content