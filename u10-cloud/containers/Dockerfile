FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
#COPY server.py app/server.py
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "./server.py", "run", "--host=0.0.0.0"]
