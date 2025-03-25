FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

COPY . .

RUN poetry install -n

EXPOSE 8000

ENTRYPOINT [ "poetry" , "run" ]

CMD [ "uvicorn", "classroom.wsgi" ]