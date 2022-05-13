FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN apt update && apt install -q --assume-yes curl

COPY script .

CMD ./script
