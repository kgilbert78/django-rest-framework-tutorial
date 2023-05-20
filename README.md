# Django Rest Framework Tutorial

This repo is intended to refresh and expand my Django knowledge, and to provide a commit history with diffs that are useful as a reference for future projects.

The tutorial I am following is [a YouTube playlist by Code Environment](https://www.youtube.com/playlist?list=PLmDLs7JbXWNjr5vyJhfGu69sowgIUl8z5) with [this accompanying GitHub repo](https://github.com/CodeEnvironment/django-rest-framework-code)

## To install this project:

(with empty databases)

1. clone it: `git clone https://github.com/kgilbert78/django-rest-framework-tutorial.git`

2. `cd django-rest-framework-tutorial`

3. [create a virtualenv, activate it](https://www.youtube.com/watch?v=N5vscPTWKOk), and `pip install -r requirements.txt`

4. [generate a secret key](https://www.educative.io/answers/how-to-generate-a-django-secretkey) using `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` and copy it to the clipboard

5. `cd main_api/main_api/` (directory which contains `settings.py`), create a file called `.env` and put in it `SECRET_KEY = ''` with the newly generated secret key pasted in between the quotes

6. `cd ..` to the same level as `manage.py`, and `python manage.py migrate`

7. from that same directory `python manage.py runserver`

## Resources

[Django Rest Framework docs](https://www.django-rest-framework.org/)

[dj-rest-auth docs](https://dj-rest-auth.readthedocs.io/en/latest/index.html), which is an update of the django rest-auth library used in the video series

[Simple JWT docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

### Commands Reference

- `python manage.py runserver`

- `python manage.py makemigrations` followed by `python manage.py migrate`

- `python manage.py shell`

- `python manage.py startapp <app-name>` to create a new app within the larger project

### Initial Setup for new empty Django project

1. create virtualenv & activate it

2. `pip install Django` and `pip install djangorestframework`

3. `django-admin startproject <project-name>`

4. `python manage.py runserver` then go to http://localhost:8000/ in the browser to check if the rocket displays

5. `python manage.py migrate` ...and then you can access the default tables in the database

6. `python manage.py startapp <app-name>` to create the first app

7. `python manage.py createsuperuser` to create admin: enter username of `admin`, email & password

8. go to http://localhost:8000/admin/ in the browser to log in the with admin credentials

9. **BEFORE PUSHING TO GITHUB, hide the secret key:**

   - create a file called `.env` in same directory as `manage.py`, and put in it `SECRET_KEY = 'copy-the-key-from-line-23-of-your-settings.py-and-paste-it-here'`

   - in terminal (with virtualenv activated): `pip install python-decouple`

   - in `settings.py` add the following import: `from decouple import config` and replace line 23 with `SECRET_KEY = config("SECRET_KEY")`

   - make sure `.env` is included in your `.gitignore` file

### Endpoint Guide

Sample for filtering cars in `cars-app` by __brand__:

- GET request to `http://localhost:8000/cars-app/car-data/Ford`

Sample for filtering cars in `cars-app` by __brand and model__:

- GET request to `http://localhost:8000/cars-app/car-data/Ford-Focus`

Samples for viewing cars in `cars-app2` by __id__:

- GET request to `http://localhost:8000/cars-app2/?id=1`

- GET request to `http://localhost:8000/cars-app2/1/` 

Sample for viewing cars in `cars-app` by __id__:

- GET request to `http://localhost:8000/cars-app/car-data/1/`

Sample for updating cars in `cars-app`:

- PUT request to `http://localhost:8000/cars-app/car-data/1/` (number at end is id of car to edit)

- JSON should follow this format, referencing owner & service_plan by id:
  ```
  {
      "owner": "1",
      "service_plan": "3",
      "car_brand": "Chevrolet",
      "car_model": "Malibu",
      "car_year": "2021",
      "car_color": "red"
  }
  ```

Sample for updating cars in `cars-app2` without typing data you're not changing:

- PATCH request to `http://localhost:8000/cars-app2/1/` (number at end is id of car to edit)

- only include the thing to update in the json body: `{"car_color": "blue"}`

Sample for updating cars in `cars-app` without typing data you're not changing:

- PATCH request to `http://localhost:8000/cars-app/car-data/1/` (number at end is id of car to edit)

- only include the thing to update in the json body: `{"service_plan": 2, "car_color": "red"}`