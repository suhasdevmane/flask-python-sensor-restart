# flask-python-sensor-restart
flask-python-sensor-restart for turning on off sensor with smart plugs meross rss310. 

Use Docker-compose up --build on first use. 
write the docker-compose.yml with following lines of code
version: "3.0"
services:
  flask-web-app:
    build:
      context: ./flask-python
      dockerfile: Dockerfile
    container_name: flask-web-app
    volumes:
      - ./flask-python/:/app
    ports:
      - "5000:5000"
