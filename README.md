# CBD-TweetMaps
CBD Proyecto


## Docker Hub y docker-compose

La otra opción para lanzar la aplicación es descargar el fichero docker-compose.yml presente en la rama Docker [fichero](https://github.com/miguelpantoja89/CBD-TweetMaps/blob/Docker/TweetMaps/docker-compose.yml) .

Una vez descargado el fichero solamente se debe lanzar el siguiente comando:
```docker-compose up -d```

Una vez ejecutado el comando se realizará un pull de la imagen de mongo y de la imagen de la aplicación presente en [docker hub](https://hub.docker.com/r/miqpanbas/cbd-tweetmaps), a continuación, se crea el contenedor y solamente se deberá acceder a [localhost](http://localhost:8000)

