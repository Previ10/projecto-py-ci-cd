Proyecto Python Flask con Docker y CI/CD
Este proyecto es una aplicación Python Flask que se configura para ser ejecutada en un entorno Docker y se integra con DockerHub a través de un flujo de trabajo de integración continua en GitHub Actions. A continuación, se detalla el proceso de configuración y despliegue del proyecto.

Estructura del Proyecto
1. Estructura de Archivos
app.py: Archivo principal de la aplicación Flask.
config.py: Archivo de configuración que carga variables de entorno para la conexión a la base de datos.
index.py: Script para inicializar la base de datos.
Dockerfile: Dockerfile para construir la imagen de producción.
Dockerfile-develop: Dockerfile para el entorno de desarrollo.
.env: Archivo de variables de entorno para la configuración local (no incluido en el repositorio).
requirements.txt: Archivo de dependencias de Python.
src/: Directorio que contiene el código fuente del proyecto.


2 Instrucciones de Ejecución
Para ejecutar el entorno de desarrollo:
´´bash
docker build -f Dockerfile-develop -t proyecto-python-dev:latest .
Ejecutar el contenedor:

´´bash
docker run -p 5000:5000 proyecto-python-dev:latest
Para ejecutar el entorno de producción:

Construir la imagen Docker para producción:

´´bash
docker build -t proyecto-python:latest .
Ejecutar el contenedor:

´´bash
docker run -p 5000:5000 proyecto-python:latest
8. Despliegue en DockerHub
Asegúrate de tener configurados los secretos DOCKER_USERNAME y DOCKER_PASSWORD en tu repositorio de GitHub. Estos se utilizan para autenticar y subir imágenes a DockerHub.

Para activar el flujo de trabajo de CI/CD:

Realiza un push a la rama main o crea una solicitud de extracción (pull request) a main.

GitHub Actions construirá y subirá la imagen Docker automáticamente.

Este README proporciona una visión general completa de la configuración y despliegue de tu aplicación Python Flask con Docker y GitHub Actions. Asegúrate de ajustar las configuraciones específicas según las necesidades de tu proyecto.