FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
