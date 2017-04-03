all: update_static deploy

BUCKET=$(shell grep bucket: app_settings.yaml | cut -d' ' -f2)
CLOUDSQL=$(shell grep cloudsql_connection: app_settings.yaml | cut -d' ' -f2)

update_static:
	python manage.py collectstatic --noinput
	gsutil -m rsync -x ".*DS_Store" -R static gs://$(BUCKET)/static

deploy:
	gcloud app deploy

sql:
	cloud_sql_proxy -instances="$(CLOUDSQL)"=tcp:3306
