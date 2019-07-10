FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code
RUN pip install -r requirements.txt
CMD bash -c "python manage.py collectstatic --no-input;python manage.py migrate;python manage.py runserver 0.0.0.0:8000"
