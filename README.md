# Implementación de Calculadora con ANTLR
# Guía paso a paso para instalar ANTLR en sistema Linux

## *Pasos*

### *1. Descargar ANTLR*
   - *Descripción:* Primero, descarga el archivo antlr-4.12.0-complete.jar desde el sitio oficial de ANTLR.
     bash
     wget https://www.antlr.org/download/antlr-4.12.0-complete.jar -P ~/Descargas/
     

### *2. Configurar el CLASSPATH*
   - *Descripción:* Añade el archivo antlr-4.12.0-complete.jar al CLASSPATH de tu sistema para que esté disponible en cualquier sesión de terminal.
     bash
     export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.12.0-complete.jar:$CLASSPATH"
     

#### *2.1. Editar el archivo de configuración del shell*
   - *Descripción:* Abre el archivo de configuración de tu shell en tu editor de texto favorito. Por ejemplo, con Sublime Text:
     bash
     subl ~/.bashrc
     

#### *2.2. Añadir la configuración del CLASSPATH*
   - *Descripción:* Añade la siguiente línea al final del archivo:
     bash
     export CLASSPATH=
