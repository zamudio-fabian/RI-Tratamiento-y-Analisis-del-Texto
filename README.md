# RI - Recuperación de información
@author - Zamudio Fabian (2017)

Repositorio de Recuperación de Información

### Ejemplo de uso
python main.py ~/code/RI-Tratamiento-y-Analisis-del-Texto/demo-data ~/code/RI-Tratamiento-y-Analisis-del-Texto/palabras-vacias.txt

### Ejercicio

Escriba un programa que realice operaciones simples de análisis léxico sobre la colección T12012-gr y calcule medidas básicas sobre la misma. Su programa debe recibir como parámetros el directorio donde se encuentran los documentos y un argumento que indica si se deben eliminar las palabras vacías (y en tal caso, el nombre del archivo que las contiene). 
Defina, además, una longitud mínima y máxima para los términos. Como salida, el programa debe generar:

* a) Un archivo (terminos.txt) con la lista de términos a indexar (ordenado), su frecuencia en la colección y su DF (Document Frequency).
* b) Un segundo archivo (estadisticas.txt) con los siguientes datos:
    * -Cantidad de documentos procesados
    * -Cantidad de tokens y términos extraídos
    * -Promedio de tokens y términos de un documento
    * -Largo promedio de un término
    * -Cantidad de tokens y términos del documento más corto y del más largo
    * -Cantidad de términos que aparecen sólo 1 vez en la colección
* c) Un tercer archivo con:
    * -La lista de los 10 términos más frecuentes y su CF (Collection Frequency)
    * -La lista de los 10 términos menos frecuentes y su CF.
