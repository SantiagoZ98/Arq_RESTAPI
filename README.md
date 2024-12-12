# RESTAPI with Python in Docker

A simple RESTAPI server using Python, coupled with Docker for easy execution in any environment.

## Description

This is a basic RESTAPI server implemented with PYTHON. The server listens for RESTAPI connections on port 8080 and displays a Hello World message.

### Changes:
- The server now serves an app.py file to facilitate user testing RESTAPI through a browser.
- The RESTAPI connection is established at https://localhost:8080.

## Technologies used

- python
- RESTAPI
- Docker
- FLASK

## Prerequisites

To run this project, you must have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to run the project

1. *Clone this repository:*

If you have not yet cloned the repository, you can do so with the following command:

bash
git clone git clone git clone https://github.com/SantiagoZ98/Arq_RESTAPI.git

2. **Build the Docker image:**

Before running the container, build the Docker image with the following command:

bash
docker build -t santiagozurita26/my-python-arq .

3. *Push the image to Docker Hub (if necessary):*

If you want to push the image to Docker Hub for others to use, you can do so with:

bash
docker push santiagozurita26/my-python-arq:tagname

4. **Run the Docker container:**

After building the image, run the container with the following command:

bash
docker pull santiagozurita26/my-python-arq

5. *Access the RESTAPI server:*

Once the container is running, you can connect to the WebSocket server using the following RESTAPI URL:
bash
https://localhost:8080/home

6. **Test the connection:**

-**When the user connects,** they will receive the message "Hello world, my name is Santiago Zurita."
