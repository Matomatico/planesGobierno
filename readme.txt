PLANES DE GOBIERNO : ROBOT DE TWITTER - APPENGINE
-------------------------------------------------

Este proyecto tiene la intencion de tuitear fragmentos de los planes de
gobierno de los candidatos a las Elecciones Regionales y Municipales 2014
en Peru.

REQUISITOS

- Contar con una cuenta de AppEngine
- Descargar el AppEngine SDK, Python 2.7 y las librerias necesarias.

CONFIGURACION
- app.yaml: Nombre de la app y version de la misma.
- cron.yaml: Nombre del script a programar.

NOTAS
- La liberia python-tweeter usa la cache para funcionar, entrando en conflicto
con las condiciones de Google App Engine.
- Se usa la libreria requests version 1.2.3
- Se incluye la libreria SSL para AppEngine en app.yaml.

JSON
/d/d.py
{
  "u" : ubigeo
  "o" : organizacion politica
  "t" : tipo ( solucion o meta )
  "n" : numero de dimension ( social, economica, ambiental, institucional )
  "c" : contenido del plan
}

/d/l.py
{
  "nn0000" : ubigeo de la region
  {
    "codigo de partido" : "enlace corto de plan de gobierno completo"
  }
}

TO DO
- Construir scrapper para recopilar toda la informacion automaticamente.