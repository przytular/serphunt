# SERP Scraper

Google keywords scraper written in Django and JavaScript.

## Getting Started

This is Django application for searching keyword on google website and creating statistics.

### Prerequisities

In order to run this containers you'll need docker and docker-compose installed.

[Install Docker](https://docs.docker.com/install)

### Development

Frontend is handled by npm and webpack. There is also webpack-dev-server running on localhost:8080 for static files and auto-reloading in development process.

#### Run services

```shell
$ docker-compose up
```

After couple of minutes to boot there should be a development server running at http://localhost/
