install:
	poetry install

lint:
	poetry run flake8 task_manager

dev:
	poetry run python manage.py runserver

start:
	poetry run gunicorn task_manager.asgi:application --bind 0.0.0.0:80

migrate:
	poetry run python manage.py migrate

build:
	./build.sh