## PROYECTO PYTUBE 

En este proyecto vamos a crear un contenedor en el cual vamos a ejecutar un script en Python

El script utilizará la librería externa pytube (pytube==12.1.2). Esta será necesario añadirla en el archivo "Dockerfile" haciendo referencia a "requirements.txt".
```
Dockerfile: RUN pip install requirements.txt
```
```
requirements.txt: pytube==12.1.2
```
El documento Dockerfile quedará de la siguiente manera:
```
FROM python:3

WORKDIR /usr/src/app

RUN pip install requirements.txt

COPY ./app /usr/src/app/

CMD ["python", "main.py"]
```
Se deberá empezar el proceso descargando la imagen de python, ya que será necesaria para poder realizar la tarea. Esto se puede realizar en la terminal.
```
  docker pull python:3
```
También será necesario construir la imagen, para ello se deberá utilizar el comando "build" y darle un nombre a la imagen:
```
  docker build -t youtubeimagen:latest 
```
Posteriormente configurará el docker-compose.yml de la siguiente manera:
```
services:
    python:
        image: youtubeimagen:latest
        volumes:
            - ./app:/usr/src/app
        working_dir: /usr/src/app
        command: python main.py
```
Finalmente y para levantar el servicio deberá utilizar el comando:

```
$ docker-compose up
```
Para subir la nueva imagen a DockerHub será necesario tener una cuenta previamente creada y validada. Desde la terminal escribiremos los siguientes comandos para hacer un push de la imagen:
```
 docker login
  
 docker tag youtubeimagen:latest alberto_420/youtubeimagen:latest .
  
 docker push alberto_420/youtubeimagen:latest
```
El enlace de nuestro repositorio para dockerhub es el siguiente: [YouTubeImagen de Mateo](https://hub.docker.com/repository/docker/alberto420/youtubeimagen/general).
