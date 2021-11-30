# Ecommerce platform

Django core

# Install

## What do you need before start?

- Install Docker https://docs.docker.com/engine/install/
- Install docker-compose https://docs.docker.com/compose/install/
- You must have a pair of valid ssh keys set to run the project.

## Verify version docker and docker-compose

```bash
# Check docker compose version
docker-compose --version
## The project is running in Docker Compose version v2.0.0-rc.3
# Check docker version
docker --version
## The project is runnin in docker version Docker version 20.10.8, build 3967b7d
```

### Download and install on MAC

https://docs.docker.com/docker-for-mac/install/

# Try it out in environment DEV:

```bash
# To rebuild all changes
docker-compose down -v
# Build image
docker-compose up -d --build
# Makemigrations
docker-compose exec web python manage.py makemigrations
# Make migrations
docker-compose exec web python manage.py migrate --noinput
# Make collestaticfiles
docker-compose exec web python manage.py collectstatic --no-input --clear
# Create superuser
docker-compose exec web python manage.py createsuperuser
```
