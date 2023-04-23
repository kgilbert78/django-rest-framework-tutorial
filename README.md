# Django Rest Framework Tutorial

This repo is intended to refresh and expand my Django knowledge, and to provide a commit history with diffs that are useful as a reference for future projects.

The tutorial I am following is [a YouTube playlist by Code Environment](https://www.youtube.com/playlist?list=PLmDLs7JbXWNjr5vyJhfGu69sowgIUl8z5) with [this accompanying GitHub repo](https://github.com/CodeEnvironment/django-rest-framework-code)

To install this project `pip install -r requirements.txt`

## Resources

[Django Rest Framework docs](https://www.django-rest-framework.org/)

[dj-rest-auth docs](https://dj-rest-auth.readthedocs.io/en/latest/index.html), which is an update of the django rest-auth library used in the video series

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
