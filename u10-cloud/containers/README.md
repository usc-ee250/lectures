https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

Create a flask server
Create a requirements.txt

```
Flask
```

create a Dockerfile

```
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
```

Build the docker image

docker build -t my-flask-app .

Run the Docker container


docker run -d -p 5000:5000 my-flask-app


Access your flask server

Open your web browser and navigate to http://localhost:5000/ to see your Flask app running inside the Docker container.

