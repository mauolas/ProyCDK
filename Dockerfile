FROM python:3.7-alpine

ADD  ./src /code

WORKDIR /code

RUN pip install -r dependences.txt

CMD ["python", "WebService.py"]
