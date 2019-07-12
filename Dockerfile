FROM nikolaik/python-nodejs:python3.7-nodejs8
ENV PYTHONUNBUFFERED 1
ADD . /code
WORKDIR /code
RUN npm install --loglevel=error
RUN pip install -r requirements.txt
