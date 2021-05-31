build: init generate-static
dev-build: init test-init test
test:
	python manage.py test

init:
	pipenv sync && python manage.py migrate && python manage.py loaddata init

generate-static:
	python manage.py collectstatic --no-input

test-init:
	python manage.py loaddata test
