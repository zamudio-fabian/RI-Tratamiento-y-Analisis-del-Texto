# RI - Recuperación de información
@author - Zamudio Fabian (2017)

Repositorio de Recuperación de Información

### Ejemplo de uso
python main.py ~/code/RI-Tratamiento-y-Analisis-del-Texto/demo-data ~/code/RI-Tratamiento-y-Analisis-del-Texto/palabras-vacias.txt

### Ejercicio

Tomando como base su programa anterior, escriba un segundo Tokenizer que implemente
los criterios del artículo de Grefenstette y Tapanainen para definir qué es una “palabra” (o
término) y cómo tratar números y signos de puntuación. Luego, antes de tokenizar extraiga
en listas separadas:

* • Abreviaturas tal cual están escritas (por ejemplo, Dr., Lic., S.A., NASA, etc.)
* • Direcciones de correo electrónico y URLs
* • Números (por ejemplo, cantidades, teléfonos)
* • Nombres propios (por ejemplo, Villa Carlos Paz, Manuel Belgrano, etc.) y los trate como un único token.

Genere y almacene la misma información que en caso anterior