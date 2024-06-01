# Usar la imagen oficial de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Exponer el puerto 80 para la aplicación Flask dentro del contenedor
EXPOSE 80

# Ejecutar la aplicación Flask cuando el contenedor se inicia
CMD ["python", "main.py"]