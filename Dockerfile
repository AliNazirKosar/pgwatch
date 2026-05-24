# Imagen base — Python 3.12 versión ligera (sin herramientas innecesarias)
FROM python:3.12-slim

# Carpeta de trabajo dentro del contenedor — aquí vivirá el código
WORKDIR /app

# Copia el listado de dependencias desde tu máquina al contenedor
COPY requirements.txt .

# Instala todas las dependencias de Python dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . .

# Puerto que usa la API — Docker lo documenta para saber por dónde escucha
EXPOSE 8000

# Comando que se ejecuta al arrancar el contenedor — inicia la API FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]