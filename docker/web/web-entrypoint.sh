#!/bin/bash

# Collect static files
python manage.py collectstatic --no-input

# Migrate database changes
python manage.py migrate

# Webpack compile
npm run build

# Start webpack development server
npm start &

# Start django development server
python manage.py runserver 0.0.0.0:8000
