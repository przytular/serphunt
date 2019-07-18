#!/bin/bash

# Collect static files
python manage.py collectstatic --no-input

# Migrate database changes
python manage.py migrate

# Webpack compile
npm run build

# Start webpack development server
npm start &

# Collect user agents
python manage.py scrape_user_agents

# Start django development server
python manage.py runserver 0.0.0.0:8000

# Start production server (gunicorn)
# gunicorn _core.wsgi:application -b 0.0.0.0:8000 --reload