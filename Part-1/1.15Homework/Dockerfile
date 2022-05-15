# as a base image use the debian 11 based python 3.11 image
FROM python:3.11.0b1-bullseye

# set workdir
WORKDIR /usr/var/app

# copy the python script in 
COPY ./check_if_odd.py .

# set the initial command
CMD [ "python3", "./check_if_odd.py" ]

