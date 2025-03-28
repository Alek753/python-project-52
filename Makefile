build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv pip install -r requirements.txt

migrate:
	uv run python3 manage.py makemigrations && uv run python3 manage.py migrate

dev:
	uv run python3 manage.py runserver
