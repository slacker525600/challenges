FROM python:3.9

RUN mkdir /code
COPY  . /code/

WORKDIR /code/

ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "python3", "entrypoint.py" ]
