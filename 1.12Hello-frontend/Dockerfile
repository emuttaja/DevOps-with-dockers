# pull node container that's based on debian 11 from dockerhub (I guess the project works only on node version 16..)
FROM node:16-bullseye

# set workdir
WORKDIR /usr/src/app

# copy the project
COPY . .

# Install all packages needed
RUN npm install

# start the project in production mode
# build the project
RUN npm run build
# install the serve package
RUN npm install -g serve

# finally host the project on porrt 5000
CMD serve -s -l 5000 build
