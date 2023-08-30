1. Start redis on port 6379 `sudo service redis-server start`
2. Start postgres on port 5432 and create a new database called 'task'
3. Install requirements with `pip install -r requirements.txt`
4. Start django app `python manage.py runserver`
5. Create a few users with `djangoadmin createsuperuser` (login with django admin)
6. Start celery worker `celery -A TestTask.celery worker --loglevel=info -P eventlet` (if the order creation is slow try creating two workers.)
7. Start celery beat `celery -A TestTask beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler`
