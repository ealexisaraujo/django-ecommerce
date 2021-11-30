SHELL := /bin/bash

build-docker-dev:
	git pull
	docker-compose down -v
	docker-compose up -d --build

start-dev:
	docker-compose up -d

stop-dev:
	docker-compose stop

clean-dev:
	docker-compose down -v

ssh-dev:
	@if [ "$(shell uname -s)" == "Darwin" ]; then \
		( docker exec -it -w /usr/src/app greatkart-web-1 sh ); \
	else \
		( docker exec -it -w /usr/src/app greatkart-web-1 zsh ); \
	fi;

superuser:
	docker-compose exec web sh -c "cd /usr/src/app && ./manage.py createsuperuser"

restart-dev:
	docker-compose restart web