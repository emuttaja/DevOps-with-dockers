# command used to start the container: elias@debian:~/hacking/devops_with_dockers/material-applications/material-applications/example-backend$ docker run -p 8080:8080 example-backend

# pull a debian 11 based golang 1.16 image from dockerhub
FROM golang:1.16.15-bullseye

# set workdir
WORKDIR /usr/src/app

# copy the project
COPY . .

# build it 
RUN go build

# start the project with needed environment variables
CMD PORT=8080 ./server
