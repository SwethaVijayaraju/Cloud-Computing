## Create a Docker network
```
docker network create mynetwork
```

## Postgres DB

Build:
```
cd db
docker build -t my_db .
```

Run:
```
docker run --name mydb --network mynetwork -p 5432:5432 -d my_db
```

## PGAdmin

Build:
```
cd dbadmin
docker build -t my_dba .
```

Run:
```
docker run --name mydba --network mynetwork -p 8081:80 -d my_dba
```

## Django App

Build:
```
docker build -t my_django .
```

Run:
```
docker run --name mydjango -p 8000:8000 --network mynetwork  mydjango
```


Initial Project Creation:

1. Create a new directory on the host e.g `app`.
2. Run the `mydjango` container with volume mapping so that the project 
   can be created within the container using `django-admin` and would show up 
   on the host as well.

```
docker run --rm -it --name mydjango -p 8000:8000 -v "$(pwd)/app:/app" --network mynetwork --entrypoint /bin/bash mydjango
```

```
django-admin startproject ap
```
 
