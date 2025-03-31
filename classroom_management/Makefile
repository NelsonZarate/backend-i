install-dependencies:
	poetry add django uvicorn sqlmodel psycopg2-binary pytest django-pytest whitenoise 
	poetry install

start:
	poetry run python manage.py runserver

migrate:migration
	poetry run python manage.py migrate

migration:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser

newapp:
	poetry run python manage.py startapp ${app}
	@# to execute run `make newapp app=Etic`

test:
	poetry run pytest

compose.migrations:
	docker compose run --rm web poetry run python manage.py makemigrations

compose.migrate:
	docker compose run --rm web poetry run python manage.py migrate


compose.start:
	docker compose up --build --force-recreate

compose.collectstatic:
	docker compose exec web poetry run python manage.py collectstatic --noinput

compose.createsuperuser:
	docker compose exec web poetry run python manage.py createsuperuser

compose.test:
	docker compose exec web poetry run python manage.py test
	