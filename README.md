# SERP Scraper

Google keywords scraper written in Django and JavaScript. It can spoof fake user agent and use proxies. If user is authenticated, history of scraper requests are saved in the database.


## Prerequisities

In order to run this containers you'll need docker and docker-compose installed.

* [Install Docker](https://docs.docker.com/install)
* [Install Docker-compose](https://docs.docker.com/compose/install/)


## Getting Started

#### Create .env file from template

```shell
$ cp .env.example .env
```

#### Run docker-compose up

```shell
$ docker-compose up
```

#### Create user for testing

```shell
$ docker-compose exec web python manage.py createsuperuser
```

#### Log in

Open browser at http://localhost:8000/accounts/login/

And Viola! You can start using an app.


## Development

Frontend is handled by npm and webpack. There is also webpack-dev-server running on localhost:8080 for static files and auto-reloading in development process.


## Useful commands (web container)

Scrape browser user agents from useragentstring.com (already done on docker-compose up)
```shell
$ ./manage.py scrape_user_agenst
```
