# Integrantes 

1. David Martinez
2. Franco Comas
3. ANtony Brahona

# Instalación de ANTLR en Linux

Guía paso a paso para instalar ANTLR en sistema Linux y configurarlo correctamente.

## 1. Descargar ANTLR

Primero, descarga el archivo `antlr-4.x-complete.jar` desde el sitio oficial de ANTLR.

wget https://www.antlr.org/download/antlr-4.12.0-complete.jar -P ~/Descargas/

## 2. Configurar el CLASSPATH

Añade el archivo antlr-4.x-complete.jar al CLASSPATH de tu sistema para que esté disponible en cualquier sesión de terminal.

export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.x-complete.jar:$CLASSPATH"

## 2.1. Editar el archivo de configuración del shell

Abre el archivo de configuración de tu shell en tu editor de texto favorito: 

Sublime Text: subl ~/.bashrc

## 2.2. Añadir la configuración del CLASSPATH

Añade la siguiente línea al final del archivo:

export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.x-complete.jar:$CLASSPATH"

Reemplaza TuUsuario con tu nombre de usuario real y ajusta la ruta si moviste el archivo .jar a otra ubicación.

## 2.3. Guardar y aplicar los cambios

Guarda el archivo y luego ejecuta el siguiente comando para aplicar los cambios:

source ~/.bashrc

## 3. Probar la instalación

Para verificar que ANTLR se ha instalado correctamente, puedes probarlo ejecutando el siguiente comando en la terminal:

java -jar ~/Descargas/antlr-4.x-complete.jar -version

java org.antlr.v4.Tool

Deberías ver la versión de ANTLR como salida, confirmando que está funcionando correctamente.

# Implementación de Calculadora con ANTLR

## Descripción

Esta guía describe el proceso de implementación de una calculadora simple utilizando ANTLR para el análisis léxico y sintáctico. La calculadora puede realizar operaciones aritméticas básicas y manejar expresiones dentro de paréntesis y valores absolutos.

Pasos

1. Definir la Gramática

Archivo: Calc.g4

Este archivo define la gramática para la calculadora, que incluye tanto las reglas de análisis léxico como las de análisis sintáctico. La gramática se encarga de identificar números, operadores y las estructuras de las expresiones matemáticas.

2. Generar Lexer y Parser

Utiliza ANTLR para generar el lexer y el parser a partir del archivo de gramática. Ejecuta el siguiente comando:

antlr4 Calc.g4 -Dlanguage=Python3

3. Implementar el Visitante para Evaluar Expresiones

Archivo: CalcMain.py

Implementa un visitante que procesará el árbol de parseo y evaluará las expresiones matemáticas basadas en la gramática definida. Este archivo también maneja la entrada del usuario y muestra los resultados.

4. Ejecutar la Calculadora

Para ejecutar la calculadora, asegúrate de que todos los archivos generados por ANTLR estén en el mismo directorio que CalcMain.py, y luego ejecuta el archivo Python:

python3 CalcMain.py

Esto iniciará la calculadora, permitiéndote ingresar expresiones matemáticas para evaluarlas.

# Pruebas Funcionales

