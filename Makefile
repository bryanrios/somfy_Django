all: update_static deploy

update_static:
	python manage.py collectstatic --noinput
	gsutil -m rsync -x ".*DS_Store" -R static gs://django_somfy-iot/static

deploy:
	gcloud app deploy

sql:
	cloud_sql_proxy -instances="somfy-iot:europe-west1:django-db"=tcp:3306
