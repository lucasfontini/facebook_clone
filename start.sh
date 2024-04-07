#!/bin/bash

# Iniciar o PostgreSQL e o Redis
service postgresql start
service redis-server start

# Migrar banco de dados e criar usuário superadmin
python3 manage.py migrate
echo "from django.contrib.auth.models import User; \
User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell

# Iniciar Celery Worker e Beat
celery -A facebook_clone worker --loglevel=INFO &
celery -A facebook_clone beat -l INFO &

# Iniciar servidor Django
python3 manage.py runserver 0.0.0.0:8000
