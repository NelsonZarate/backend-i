
start:
	poetry run python manage.py runserver

migrate:migration
	poetry run python manage.py migrate

migration:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser

newapp:
	poetry run python manage.py startapp $(app)
	@# to execute run `make newapp app=cenas`

test:
	poetry run pytest

compose.migrate:
	docker compose run --rm	web poetry run python manage.py migrate

compose.start:
	docker compose up --build --force-recreate