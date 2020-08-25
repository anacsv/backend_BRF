# backend_DRF


1- Install the requirements

Download or clone the project into your preferred folder.
In a CMD, browse to your folder.
Create/Activate the virtual enviroment.
Install the "requirements.txt"
py -m pip install -r requirements.txt

2- Django Migrate

Run the migrations:
py manage.py migrate

3- Import Authors

Run the custom command:
py manage.py import_authors authors.csv

4- Run tests

Run the tests:
py manage.py test

OK

Destroying test database for alias 'default'

5- Create a superuser

Run the command:
py manage.py createsuperuser

6- Run server and login

Run the command:

py manage.py runserver

In your Browser access this link: http://127.0.0.1:8000/admin
Should appear a login page, log in.
