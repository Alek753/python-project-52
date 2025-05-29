build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

migrate:
	uv run python3 manage.py makemigrations && uv run python3 manage.py migrate --run-syncdb

dev:
	uv run python3 manage.py runserver

lint:
	uv run ruff check .

test:
	uv run python3 manage.py test