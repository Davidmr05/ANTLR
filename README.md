# Instalación de ANTLR en Linux

Guía paso a paso para instalar ANTLR en sistema Linux y configurarlo correctamente.

## 1. Descargar ANTLR

Primero, descarga el archivo `antlr-4.x-complete.jar` desde el sitio oficial de ANTLR.

wget https://www.antlr.org/download/antlr-4.12.0-complete.jar -P ~/Descargas/

## 3. Configurar el CLASSPATH

Añade el archivo antlr-4.x-complete.jar al CLASSPATH de tu sistema para que esté disponible en cualquier sesión de terminal.

## 3.1. Editar el archivo de configuración del shell

Abre el archivo de configuración de tu shell en Sublime Text:

subl ~/.bashrc

## 3.2. Añadir la configuración del CLASSPATH

Añade la siguiente línea al final del archivo:

export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.x-complete.jar:$CLASSPATH"

Reemplaza TuUsuario con tu nombre de usuario real y ajusta la ruta si moviste el archivo .jar a otra ubicación.

## 3.3. Guardar y aplicar los cambios

Guarda el archivo y luego ejecuta el siguiente comando para aplicar los cambios:

source ~/.bashrc

## 4. Probar la instalación

Para verificar que ANTLR se ha instalado correctamente, puedes probarlo ejecutando el siguiente comando en la terminal:

java -jar ~/Descargas/antlr-4.12.0-complete.jar -version

Deberías ver la versión de ANTLR como salida, confirmando que está funcionando correctamente.
