#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from models.LimpiarHtmlTagsRegla import *
from models.MinusculasRegla import *
from models.TranslateRegla import *
from models.LimpiadoBasicoRegla import *
from models.MinMaxCaracteresRegla import *
from models.Termino import *
from models.Documento import *

class TokenRepository:

    terminos = {}
    tokens = []
    reglasDocumento = []
    reglasTokens = []
    documentos = []
    fileNameTerminos = "results/terminos.txt"
    lista_vacias = []

    def __init__(self):
        self.reglasDocumento.append('MinusculasRegla')
        self.reglasDocumento.append('TranslateRegla')
        self.reglasDocumento.append('LimpiarHtmlTagsRegla')
        self.reglasDocumento.append('LimpiadoBasicoRegla')
        self.reglasTokens.append('MinMaxCaracteresRegla')

    def tokenizar(self,documentos, **options):
        # INIT
        self.documentos = documentos
        self.tokens = []
        self.terminos = {}
        self.lista_vacias = []
        pathVacias = options.get('pathVacias', None)

        if pathVacias != None :
            with codecs.open(pathVacias, mode='rt', encoding='utf-8') as vacias:
                content = vacias.read()
                for regla in self.reglasDocumento:
                    instancia = globals()[regla](content)
                    content = instancia.run()

                palabras = content.strip().split()
                for palabra in palabras:
                    if palabra not in self.lista_vacias:
                        self.lista_vacias.append(palabra)

        # Procesamos cada documento
        for documento in documentos:
            content = documento.content
            # Aplicamos cada regla definida en self.reglasDocumento para normalizar
            for regla in self.reglasDocumento:
                instancia = globals()[regla](content)
                content = instancia.run()
            # Sacamos tokens de documentos
            tokensAux = self.getTokens(content)
            self.tokens = self.tokens + tokensAux
            documento.tokens = tokensAux

            # Aplicamos cada regla definida en self.reglasTokens
            for regla in self.reglasTokens:
                instancia = globals()[regla](tokensAux)
                tokensAux = instancia.run()

            # Sacamos palabras vacias
            if pathVacias != None :
                for token in tokensAux:
                    if token in self.lista_vacias:
                        tokensAux.remove(token)

            terminosAux = self.getTerminos(tokensAux,documento)
            documento.terminos = terminosAux

        self.saveTerminos()
        # Armamos la respuesta
        response = {}
        response['terminos'] = self.terminos
        response['tokens'] = self.tokens
        response['documentos'] = documentos
        return response

    def getTokens(self,string):
        content = string.strip().split()
        # Return
        return content

    def getTerminos(self,tokens,documento):
        terminos = {}
        for token in tokens:
            if token not in terminos:
                terminos[token] = Termino(token,1,documento)
            else:
                termino = terminos[token]
                termino.addCf()
                termino.addDoc(documento)
                
            if token not in self.terminos:
                self.terminos[token] = Termino(token,1,documento)
            else:
                termino = self.terminos[token]
                termino.addCf()
                termino.addDoc(documento)
        return terminos

    def saveTerminos(self):
        with codecs.open(self.fileNameTerminos, mode="w", encoding="utf-8") as archivo:
            index = 0
            archivo.write('ID'.ljust(6))
            archivo.write('|')
            archivo.write('TERMINO'.ljust(30))
            archivo.write('|')
            archivo.write('CF'.ljust(6))
            archivo.write('|')
            archivo.write('DF'.ljust(6))
            archivo.write('\n')
            archivo.write('-'*50)
            archivo.write('\n')
            for termino in sorted(self.terminos.keys()):
                archivo.write(str(index).ljust(6))
                archivo.write('|')
                archivo.write(self.terminos[termino].label.ljust(30))
                archivo.write('|')
                archivo.write(str(self.terminos[termino].CF).ljust(6))
                archivo.write('|')
                archivo.write(str(len(self.terminos[termino].DOCS)).ljust(6))
                archivo.write('\n')
                index += 1