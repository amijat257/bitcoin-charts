run:
	python manage.py runserver

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

fetch:
	python manage.py fetch_records

fixtures:
	python manage.py loaddata currencies.json
	python manage.py loaddata markets.json

venv:
	pip install virtualenv
	virtualenv -p python3 venv
	source venv/bin/activate

req:
	pip install -r requirements.txt

setup:
	python manage.py migrate
	python manage.py loaddata currencies.json
	python manage.py loaddata markets.json
	python manage.py fetch_records