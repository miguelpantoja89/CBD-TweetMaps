# CBD-TweetMaps
CBD Proyecto

El sistema operativo utilizado para realizar el proyecto es Windows 10, por lo que la configuración detallada a continuación se basará en ello.

## Lanzamiento de la aplicación
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
