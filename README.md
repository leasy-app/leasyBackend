# leasyBackend
Backend Server for Leasy System (User Application + Admin Panel)

## Technologies
* Python
* Django Framework
* Rest API
* PostgreSQL

## Libraries used
* Django v3.1.2
* djangorestframework v3.12.1
* psycopg2 v2.8.6
* pytz v2020.1
* sqlparse v0.4.1
* gunicorn v20.0.4
* asgiref v3.2.10 

## Run
1. Clone And Install Requirements
2. Launch Server via:

```bash
gunicorn djangoProject.wsgi
```

3. Access polls and django admin with [http://127.0.0.1:8000/poll](http://127.0.0.1:8000/poll) or [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
