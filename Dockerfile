FROM nikolaik/python-nodejs:python3.7-nodejs12
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN npm install
RUN pip install -r requirements.txt
