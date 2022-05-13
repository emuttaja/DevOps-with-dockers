# get Java 8 from dockerhub
FROM openjdk:8-jdk-oraclelinux7

# set workdir
WORKDIR /usr/src/app

# copy the project 
COPY . .

# build the project 
RUN ./mvnw package

# start the project
CMD java -jar ./target/docker-example-1.1.3.jar
