# RESTAPI with Python in Docker

A simple RESTAPI server using python, dockerized for easy execution in any environment.

## Description

This is a basic WebSocket server implemented with Node.js. The server listens for RESTAPI connections on port 8080 and sends a message to all connected clients. It also logs messages received from clients.

### Changes:
- Now, the server serves an app.py file for easy RESTAPI client testing through a browser.
- RESTAPI connection is established at https://localhost:8080.

## Technologies Used

- python
- RESTAPI
- Docker
- FLASK

## Prerequisites

To run this project, you need to have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to Run the Project

1. *Clone this repository:*

   If you haven't cloned the repository yet, you can do so with the following command:

   bash
   git clone git clone git clone https://github.com/SantiagoZ98/Arq_RESTAPI.git

2. **Build the Docker image:**

   Before running the container, build the Docker image using the following command:

   bash
   docker build -t santiagozurita26/my-python-arq .

3. *Push the image to Docker Hub (if needed):*

   If you'd like to upload the image to Docker Hub for others to use, you can do so with:

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

-**When a client connects,** it will receive the message "Hello, World, my name is Santiago!".
-**If the client sends a message back to the server,** the server will log that message to the console

