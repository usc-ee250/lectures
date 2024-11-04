#!/bin/sh

#docker run -it -p 5050:5000 my-flask-app
docker run -d -p 5050:5000 --name app1 my-flask-app
docker run -d -p 5051:5000 --name app2 my-flask-app
