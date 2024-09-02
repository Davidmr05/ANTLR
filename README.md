# Integrantes 

1. David Martinez
2. Franco Comas
3. Antony Brahona


# Implementación de Calculadora con ANTLR
# Guía paso a paso para instalar ANTLR en sistema Linux

## **Pasos**

### **1. Descargar ANTLR**
   - **Descripción:** Primero, descarga el archivo `antlr-4.12.0-complete.jar` desde el sitio oficial de ANTLR.
     ```bash
     wget https://www.antlr.org/download/antlr-4.12.0-complete.jar -P ~/Descargas/
     ```

### **2. Configurar el CLASSPATH**
   - **Descripción:** Añade el archivo `antlr-4.12.0-complete.jar` al CLASSPATH de tu sistema para que esté disponible en cualquier sesión de terminal.
     ```bash
     export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.12.0-complete.jar:$CLASSPATH"
     ```

#### **2.1. Editar el archivo de configuración del shell**
   - **Descripción:** Abre el archivo de configuración de tu shell en tu editor de texto favorito. Por ejemplo, con Sublime Text:
     ```bash
     subl ~/.bashrc
     ```

#### **2.2. Añadir la configuración del CLASSPATH**
   - **Descripción:** Añade la siguiente línea al final del archivo:
     ```bash
     export CLASSPATH=".:/home/TuUsuario/Descargas/antlr-4.12.0-complete.jar:$CLASSPATH"
     ```
     Reemplaza `TuUsuario` con tu nombre de usuario real y ajusta la ruta si moviste el archivo `.jar` a otra ubicación.

#### **2.3. Guardar y aplicar los cambios**
   - **Descripción:** Guarda el archivo y luego ejecuta el siguiente comando para aplicar los cambios:
     ```bash
     source ~/.bashrc
     ```

### **3. Probar la instalación**
   - **Descripción:** Para verificar que ANTLR se ha instalado correctamente, puedes probarlo ejecutando el siguiente comando en la terminal:
     ```bash
     java -jar ~/Descargas/antlr-4.12.0-complete.jar -version
     ```
     También puedes probar el siguiente comando:
     ```bash
     java org.antlr.v4.Tool
     ```
     Deberías ver la versión de ANTLR como salida, confirmando que está funcionando correctamente.

# Descripción

Esta guía describe el proceso de implementación de una calculadora utilizando Python y ANTLR para el análisis léxico y sintáctico.

## **Pasos**

### **1. Definir la Gramática**
   - **Archivo:** archivo.g4
   - **Descripción:** Este archivo define la gramática para la calculadora, incluyendo tanto las reglas de análisis léxico como las de análisis sintáctico. La gramática se encarga de identificar números, operadores y las estructuras de las expresiones matemáticas. Para generar el lexer y el parser, ejecuta el siguiente comando:
     ```bash
     antlr4 archivo.g4
     ```

### **2. Generar Lexer y Parser**
   - **Descripción:** Utiliza ANTLR para generar el lexer y el parser a partir del archivo de gramática. ANTLR es una herramienta poderosa para trabajar con gramáticas y generar analizadores léxicos y sintácticos. Primero, asegúrate de tener ANTLR y Python instalados. Luego, ejecuta los siguientes comandos:
     ```bash
     antlr4 -Dlanguage=Python3 archivo.g4
     sudo apt install python3-pip
     ```

### **3. Implementar el Visitante para Evaluar Expresiones**
   - **Archivo:** evalVisitor.py
   - **Descripción:** Implementa un visitante utilizando patrones visitantes basados en MyVisitor.py y otros archivos necesarios. Este archivo se encargará de procesar el árbol de parseo y evaluar las expresiones matemáticas basadas en la gramática definida. Además, manejará la ejecución de las expresiones aritméticas calculadas mediante el patrón visitante.

### **4. Ejecutar la Calculadora**
   - **Archivo:** calc.py
   - **Descripción:** Este archivo contiene toda la lógica final necesaria para ejecutar la calculadora. Utiliza el entorno tkinter para proporcionar una interfaz gráfica que facilite la interacción con el usuario. Ejecuta el siguiente comando para iniciar la calculadora:
     ```bash
     python3 calc.py
     ```
     Esto iniciará la calculadora, permitiéndote ingresar expresiones matemáticas para evaluarlas.


# Pruebas Funcionales

Para la prubea funcional se utilizo el t.exp: 

45

x = 7

y = 3

x + y * 4

2 * (3 + 5)

9 / 3 - 1

10 - 2 - 4 + 1

x = false

!x

x = -7

x

X = 2

Y = x++

X = 2

Y = ++x

X = 2

Y = x--

![Captura desde 2024-08-29 13-32-09](https://github.com/user-attachments/assets/d51788f3-96c1-4d21-a428-49fa0ef81fb2)


