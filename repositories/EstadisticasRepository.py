#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from models.Termino import *
from models.Documento import *

class EstadisticasRepository:

    tokens = []
    terminos = {}
    documentos = []
    fileNameTerminos = 'results/estadisticas.txt'

    def __init__(self):
        pass

    def generar(self,tokens,terminos,documentos):
        self.tokens = tokens
        self.terminos = terminos
        self.documentos = sorted(documentos, key=self.orderDocumentos)

        cantidadDocumentos = None
        cantidadTokens = None
        cantidadTerminos = None
        promedioTokens = None
        promedioTerminos = None
        largoPromedioTermino = None
        cantidadTokensDocumentoCorto = None
        cantidadTokensDocumentoLargo = None
        cantidadTerminosDocumentoCorto = None
        cantidadTerminosDocumentoLargo = None
        terminosUnaAparicion = 0

        cantidadDocumentos = len(self.documentos)
        cantidadTokens = len(self.tokens)
        cantidadTerminos = len(self.terminos)
        promedioTokens = cantidadTokens / cantidadDocumentos
        promedioTerminos = cantidadTerminos / cantidadDocumentos

        acumuladoLargoTermino = 0
        for termino in self.terminos:
            acumuladoLargoTermino += len(self.terminos[termino].label)
            if (self.terminos[termino].CF == 1):
                terminosUnaAparicion += 1

        documentoCorto = self.documentos[0]
        cantidadTerminosDocumentoCorto = len(documentoCorto.terminos)
        cantidadTokensDocumentoCorto = len(documentoCorto.tokens)

        documentoLargo = self.documentos[-1]
        cantidadTerminosDocumentoLargo = len(documentoLargo.terminos)
        cantidadTokensDocumentoLargo = len(documentoLargo.tokens)

        with codecs.open(self.fileNameTerminos, mode="w", encoding="utf-8") as archivo:
            archivo.write(u'GENERAL\n')
            archivo.write(u'='*50+'\n')
            archivo.write(u'Documentos ='+str(cantidadDocumentos)+'\n')
            archivo.write(u'Tokens totales ='+str(cantidadTokens)+'\n')
            archivo.write(u'Términos totales ='+str(cantidadTerminos)+'\n')
            archivo.write(u'Tokens promedio ='+str(promedioTokens)+'\n')
            archivo.write(u'Términos promedio ='+str(promedioTerminos)+'\n')
            archivo.write(u'Términos una sola aparición ='+str(terminosUnaAparicion)+'\n')
            archivo.write(u'\nDOCUMENTO CORTO\n')
            archivo.write(u'='*50+'\n')
            archivo.write(u'Tokens ='+str(cantidadTokensDocumentoCorto)+'\n')
            archivo.write(u'Términos ='+str(cantidadTerminosDocumentoCorto)+'\n')
            archivo.write(u'\nDOCUMENTO LARGO\n')
            archivo.write(u'='*50+'\n')
            archivo.write(u'Tokens ='+str(cantidadTokensDocumentoLargo)+'\n')
            archivo.write(u'Términos ='+str(cantidadTerminosDocumentoLargo)+'\n')

    def orderDocumentos(self,item):
        return item.tamanio

            
                
