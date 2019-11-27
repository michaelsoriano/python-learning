## To Run Django

`cd projectname`

then

`python manage.py runserver`

## to Add an App

manage.py startapp <appname>
add <appname> to INSTALLED_APPS in settings.py

## Models

- ORM -> Models iniherit from models.Model, 
- each class represent a table, 
- each variable is a db column

## Migrations

- manage.py makemigrations (GENERATES MIGRATION CODE)
- manage.py showmigrations (SHOWS THE GENERATED CODE)
- manage.py sqlmigrate <appname> <migrationname> (SHOWS THE SQL CODE)
- manage.py migrate (RUN THE MIGRATIONS)

