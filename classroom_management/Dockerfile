FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY . .

RUN poetry install -n

EXPOSE 8000

RUN poetry run python manage.py collectstatic --noinput

VOLUME ["/app"]

CMD [ "poetry" , "run" , "uvicorn", "classroom_management.asgi:application","--host","0.0.0.0","--port","8000" ]

