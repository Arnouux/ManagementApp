web: gunicorn managementapp.wsgi --log-file -
python manage.py collectstatic --noinput
manage.py migrate
