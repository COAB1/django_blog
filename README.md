installing requirements:
 $ pip install django

check if is installed:
  $ python -m django --version

# Create a new project
First of all, create the virtual environment, and then create and run the project

  install the virtual environment:
  $ pip install virtualenv

  create a virtual environment:
  $ python3 -m venv myvenv

  run virtual environment:
  $ source myvenv/bin/activate

  create requirements.txt file with versions and packages and install:
  $ pip install -r requirements.txt


create django project:
  $ django-admin startproject django_project 
  - obs: the project name can't have '-'
to run the server (will only work insode the virtual environment and inside the project folder that contain manage.py):
  $ python manage.py runserver
