# Classroom Management Tool

> Python 3.12+

## Dependencies
 - Django
 - uvicorn __ASGI web server__
 - sqlmodel
 - psycopg2-binary __Postgres Container driver__
 - pytest (Dev dependencie)
 - django-pytest (Dev dependencie)
 - whitenoise (>=6.9.0,<7.0.0)  __For serving files through ASGI with debug False__



## ENV

.env
- POSTGRES_DATABASE = 'dj_db'
- POSTGRES_USER = 'postgres'
- POSTGRES_PASSWORD = 'qwerty'
- POSTGRES_HOST = 'database' 
- POSTGRES_PORT = '5432'