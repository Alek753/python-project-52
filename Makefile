build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

migrate:
	uv run python3 manage.py migrate

dev:
	uv run python3 manage.py runserver
