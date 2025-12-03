lint: ruff

ruff:
	ruff format
	ruff check --fix

data:
	python manage.py migrate
	python -Xutf8 manage.py loaddata mysite_data.json

run:
	python manage.py runserver

