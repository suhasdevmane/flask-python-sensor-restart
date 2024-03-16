# flask-python-sensor-restart

This project aims to control sensors using smart plugs, specifically Meross MSS310, with a Flask-based web application.

## Usage

### Running the Application

To run the application for the first time, use `docker-compose up --build` command.

```yaml
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
