#!/bin/sh

#RUN apt-get update \
#&& apt-get install gcc -y \
#&& apt-get clean
# Add "RUN pip install <package-name>" for any additional packages

echo "FROM python:3.8.0-slim
RUN apt-get update \
&& apt-get clean
ADD main_app.py /$1/
ADD scripts /$1/scripts/
ADD templates /$1/templates/
RUN pip install pandas
RUN pip install xlrd
RUN pip install flask
EXPOSE $2
WORKDIR ./$1
CMD [\"python\", \"main_app.py\"]" > Dockerfile

docker build -t $1 .
docker run -d -p $2:5500 --name=$1 -v$PWD:/app $1
