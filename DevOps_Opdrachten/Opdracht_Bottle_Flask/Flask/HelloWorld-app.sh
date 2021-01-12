#!/bin/bash

mkdir tempdir

cp  FlaskDevOps.py tempdir/

echo "FROM python" >> tempdir/Dockerfile

echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install Faker" >> tempdir/Dockerfile

echo "COPY FlaskDevOps.py /home/myapp/" >> tempdir/Dockerfile

echo "EXPOSE 5000" >> tempdir/Dockerfile

echo "CMD python3 /home/myapp/FlaskDevOps.py" >> tempdir/Dockerfile

cd tempdir
docker build -t helloapp .

docker run -t -d -p 5000:5000 --name apprunning helloapp

docker ps -a
