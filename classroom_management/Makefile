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
# Create and apply migrations
compose.makemigrations:
	docker compose run --rm web poetry run python manage.py makemigrations

compose.migrate: compose.makemigrations
	docker compose run --rm web poetry run python manage.py migrate

# Collect static files
compose.collectstatic:
	docker compose exec web poetry run python manage.py collectstatic --noinput

# Create superuser
compose.createsuperuser:
	docker compose exec web poetry run python manage.py createsuperuser

# Run tests
compose.test:
	docker compose exec web poetry run python manage.py test

# Build and start containers
compose.build:
	docker compose up --build --force-recreate -d

# Start existing containers
compose.start:
	docker compose up -d

# Stop and remove containers
compose.down:
	docker compose down

# Full setup: build, migrate, collect static, create superuser
compose.setup: compose.build compose.migrate compose.collectstatic compose.createsuperuser
