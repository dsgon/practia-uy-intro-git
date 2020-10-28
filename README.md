# git101_python

Proyecto base para ejecicio introductorio a git con Python

# Intalacion Python
*  Descargar la ultima version estable de Python (3.x) desde: https://www.python.org/downloads/
*  Habilitar la opcion de *Agregar Python a la variable de entorno PATH*
*  Pueden seguir este tutorial hasta el paso 7: https://python-para-impacientes.blogspot.com/2017/02/instalar-python-paso-paso.html
*  Validar instalacion de Python via CMD con el siguiente comando: `python --version` . Deberia de mostrarle la version de Python instalada. Ej: `Python 3.x.x`

# Intalacion de IDE Visual Studio Code (VSC)
* Descargar la ultima version estable de VSC: https://code.visualstudio.com/download

# Configuracion de VSC para trabajar con Python
* Desde el menu izquierdo de VSC, en la opcion **Extensiones**, escribir **Python** e instalar el plugin de **Microsoft**.[Imagen Referencia](https://geekytheory.com/uploads/2018/08/configurar-python-visual-studio-vs-code.png)
* Una vez finalizada la instalacion, reiniciar VSC para que tome los cambios.

# Clonar Proyecto
* **Pre-condicion:** Contar con conexion via VPN a la LAN de Practia y contar con **git** instalado en tu notebook y haber creado y configurado la **Public Key** para poder obtener acceso 
al repositorio via Git.
* Desde esta misma pagina, seleccionar la opcion: `Clone >  Clone with SSH > Copy URL to clipboard`
* Desde la consola de git (Git Bash), posicionarse en el directorio donde se desea guardar el proyecto. Ej: `Documents/Escuelita`
* Ejecutar el comando: `git clone ssh://git@gitlab2.practia.global:2222/ar/practia/practiaschool/git/introduction_101.git`
* **Nota**: Si es la primera vez que realizas un clone con tu clave publica, deberas confirmas el mensaje sobre tu credencial con **yes** y luego presionar `ENTER`
dejando en vacio las siguientes opciones.


# Abrir proyecto en VSC
* **Pre condicion: Es necesario haber clonado en tu notebook el proyecto.** 
* Desde VSC seleccionar: `Archivo > Abrir Carpeta`
* Se abrira el menu contextual de Window y en el mismo buscar la carpeta del proyecto (**git101_python**) donde fue clonado,  
seleccionar y presionar **Seleccionar Carpeta**
* Se mostrara en el Explorador del VSC (lado izquierdo) la carpeta con los siguientes archivos: **git101.py** / **persona.py** 
/ **utils.py** / **README.md**

# Estructura del Proyecto
El proyecto consiste en 3 archivos python y un archivo .md
*  git101.py
*  persona.py
*  utils.py
*  README.md

El archivo `git101.py` es el archivo ejecutor, es el equivalente al main en Java. este archivo hace llamados a los archivos/clases Persona 
y Utils. 

El archivo `persona.py` es el responsable de la clase Persona, el cual contiene los atributos y metodos de dicha clase, su responsabilidad
es unicamente de la Persona. 

El archivo `utils.py` es una clase de Utilidades, el cual permite contar con metodos o funcionalidades que son 
requeridas desde el archivo 'git101.py' para complementar con la informacion que tiene la Persona.

El archivo `README.md` es esta misma Wiki, pero en formato de archivo texto.

# Como ejecutar el proyecto
1.  Desde VSC abrir una terminal/consola: `Terminal > New Terminal`
2.  Desde la terminal/consola confirmar que se ejecuta el proyecto  con la siguiente linea de comando: `git101.py`. El resultado obtenido 
deberia ser: **Hola Escuelita**

# Objetivos del Proyecto
* Conocer y utilizar los comandos Git que fueron visto en la presentacion.
* Crear Branchs, realizar commits, pushs, pulls y merges a medida se avance con el ejercico.
* Crear un metodo que devuelva el nombre completo de una Persona.
* Crear un metodo que devuelva la edad en base a una fecha de nacimiento.
* Crear instancias de personas de cada alumno/participante que se agregaran a la lista de Participantes.
* Crear una iteracion que permita recorrer la lista de Participantes y mostrar de cada uno su nombre completo (en mayuscula) y la edad que tienen.
