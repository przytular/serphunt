# SERP Scraper

Google keywords scraper written in Django and JavaScript.

## Getting Started

This is Django application for searching keyword on google website and creating statistics.

### Prerequisities

In order to run this containers you'll need docker and docker-compose installed.

[Install Docker](https://docs.docker.com/install)

### Development

You'll need .env file created in root directory that contain enviroment variables such as ALLOWED_HOSTS or DEBUG. You can copy ready template from .env.example file.

Frontend is handled by npm and webpack. There is also webpack-dev-server running on localhost:8080 for static files and auto-reloading in development process.

#### Run services

```shell
$ docker-compose up
```

### Useful commands (web container)

Scrape browser user agents from useragentstring.com
```shell
$ ./manage.py scrape_user_agenst
```
