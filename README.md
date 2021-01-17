# Platzigram
Django course project from Platzi

## Dependecies
[![Django versions](https://img.shields.io/pypi/djversions/djangorestframework)]


## Usage
Create env and install dependencies
```shell
python3 -m venv .env
source .env/bin/activate
pip install django
pip install pillow
pip install psycopg2-binary
```

Create and migrate database

Start the app
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



