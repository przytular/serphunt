FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
