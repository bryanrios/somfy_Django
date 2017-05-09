all: update_static deploy

CLOUDSQL=$(shell grep cloudsql_connection: app_settings.yaml | cut -d' ' -f2)

update_static:
	python manage.py collectstatic --noinput

deploy:
	gcloud app deploy

sql:
	cloud_sql_proxy -instances="$(CLOUDSQL)"=tcp:3306
