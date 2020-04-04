FROM python:3.7-alpine

RUN apk add unixodbc psqlodbc

ADD  ./src /code

RUN cat /code/odbcinst.ini > /etc/odbcinst.ini

WORKDIR /code

RUN pip install -r dependences.txt

CMD ["python", "WebService.py"]
