# MiPrimeraPagina-Diez

## Preentrega 3 Curso Python de CoderHouse 56060 Facundo Diez

## Resumen del proyecto
el objetivo de esta preentrega fue realizar una primera aproximacion a una pagina, 
para ello desarrolle una breve entrada de blog con el proposito de encaminar la entrega final.
Por cuestiones de tiempo por complicaciones personales no pude trabajar la parte estetica a traves de 
Bootstrap, pero va a ser diseñado para la entrega final. 

Adentrandonos en el proyecto, el blog en cuestion toma tres modelos, que son Autores, Posts y Comentarios con
el proposito de mostrar los articulos, autores y opiniones que se encuentran en la base de datos, y atraves del 
uso de formularios tambien se pueden agregar nuevas entradas a cada uno de los puntos mencionados que se almacenan en la base
de datos. 

en cuanto al funcionamiento, para poder acceder a la pagina web se corre el comando 
python manage.py runserver y se utiliza el url que brinda tal comando para entrar en la interfaz del blog 
para su funcionamiento es necesario estar en un entorno virtual activo, en este caso, al trabajar con mac el codigo para activarlo es source .venv/bin/activate 

Los atributos o display que se encuentran en cada seccion, que se vinculan a traves de los paths en las secciones de urls, 
se realizaron a traves de diversos archivos html que permiten la interaccion a traves de botones y devoluciones de informacion
a traves de tablas principlamente

Para correr el servidor, se implemento la configuracion de settings para permitir la utilizacion de las apps core y blog, y ademas se seteo los urls y caminos para el correcto funcionamiento de la pagina, permitiendo tener las secciones conectadas y entre configuracion, nucleo y proyecto.

EL nucleo o core como fue denominado sirve como base de la pagina, a traves de una funcion index. 

Con respecto a los formularios, se creo un archivo forms.py en donde se le pasaron los features de los modelos para que sean pedidos a la hora de introducir un nuevo dato en alguna de sus correspondientes secciones, determiandas por su finalizacion _add en los archivos html.

EL archivo de texto requirements determina los requisitos necesarios para poder utilizar este codigo en su conjunto, y permite instalar todo en un mismo comando.

El gitignore consiste de un archivo en donde se adjunta los archivos que se quieren omitir a la hora de publicar en github, personalmente he decidido solo poner el entorno virtual.

Ademas, se configuro la funcion de un SuperUser, que vendria a tomar el rol de administrador, que posee la capacidad de acceder a la base de datos completa, agregar y borrar entradas en una seccion especial para este mismo. 

Ademas, se ha creado un archivo base html, con el proposito de llevar a cabo la herencia de plantillas. En esta se coloca el formato base de todas las html, las cuales llevan una linea de codigo que determina la extension de la base en la primera linea de cada uno de estos archivos.
Para crear un nuevo Post siendo un autor no registrado hay que previamente registrarse en la seccion de autores
