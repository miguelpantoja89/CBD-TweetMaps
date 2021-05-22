# CBD-TweetMaps
CBD Proyecto

El sistema operativo utilizado para realizar el proyecto es Windows 10, por lo que la configuración detallada a continuación se basará en ello.

## Lanzamiento de la aplicación con mongo dockerizado y el proyecto django en local
Para lanzar el proyecto debemos crear un entorno virtual con el siguiente comando:

```python -m venv <name>```

Supongamos que nuestro entorno se llama venv, una vez creado debemos activarlo , entrando al directorio correspondiente:

```cd venv\Scripts```

Y lo activamos : 

```activate```

Una vez activado nos clonamos el repositorio en el directorio que queramos:

```git clone https://github.com/miguelpantoja89/CBD-TweetMaps.git```

Entramos al repositorio, instalamos las herramientas requeridas y lanzamos el docker el cual contiene la base de datos:

```cd CBD-TweetMaps```

```pip install -r requirements.txt```

```docker-compose up -d```

A continuación debemos entrar a la carpeta donde contenie el archivo "manage.py".

```cd TweetMaps```

Y lanzamos el siguiente comando:

```python manage.py setup```

Con ello se realizarán todas las migraciones y se creará un superuser con el usuario "admin" y la contraseña "pass". Por último ya podrá tener la aplicación en su local con el siguiente comando:

```python manage.py runserver```

## Docker Hub y docker-compose

La otra opción para lanzar la aplicación es descargar el fichero docker-compose.yml presente en la rama Docker [fichero](https://github.com/miguelpantoja89/CBD-TweetMaps/blob/Docker/TweetMaps/docker-compose.yml) .

Una vez descargado el fichero solamente se debe lanzar el siguiente comando:
```docker-compose up -d```

Una vez ejecutado el comando se realizará un pull de la imagen de mongo y de la imagen de la aplicación presente en [docker hub](https://hub.docker.com/r/miqpanbas/cbd-tweetmaps), a continuación, se crea el contenedor y solamente se deberá acceder a [localhost](http://localhost:8000)
