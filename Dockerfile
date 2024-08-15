# Usa una imagen base de Python
FROM python:3.9.7

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos
COPY src/requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación
COPY src/ /app

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
