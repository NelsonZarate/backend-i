build:
	docker compose build
start: build
	docker compose up -d --force-recreate 
down:
	docker compose down --volumes
logs:
	docker compose logs -force
api-logs:
	docker compose logs -f api

test: build
	docker compose run --rm --entrypoint="" api poetry run pytest -vvv