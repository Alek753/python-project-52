build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

migrate:
	uv run python manage.py migrate