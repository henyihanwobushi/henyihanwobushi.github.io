---
layout: post
title: "[tool] Docker Hello World"
date: 2023-09-08 00:14 +0800
---
# Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. And because containers are isolated from one another and run independently, you can also run many containers simultaneously.

Another benefit of Docker is that you can run another OS in your local machine. For example, you can run Ubuntu in your Mac OS. This is very useful when you want to compile your code in a specific OS.

## Install Docker

You can install Docker from [here](https://docs.docker.com/desktop/install/mac-install/).

Then you can run `docker run hello-world` to test if Docker is installed successfully.

## Create a Docker Image

You can create a Docker image by writing a `Dockerfile`. Here is an example:

```dockerfile
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y build-essential gcc g++ && \
    apt-get clean
```

Then you can build the image by running `docker build -t ubuntu:18.04 .` in the same directory as the Dockerfile.

## Run a Docker Container

You can run a Docker container by running `docker run -it ubuntu:18.04 /bin/bash`. This will run a container with Ubuntu 18.04 and you can use the bash in the container.

## Maintance Containers

You can show all containers by running `docker ps -a`.
You can remove a container by running `docker rm <container id>`. Or you can also remove all containers by running `docker rm $(docker ps -a -q)`.

## Maintance Images

You can show all images by running `docker images`.
You can remove an image by running `docker rmi <image id>`. Or you can also remove all images by running `docker rmi $(docker images -q)`.