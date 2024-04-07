from django_celery_beat.schedulers import DatabaseScheduler
from datetime import datetime, timezone

class CustomDatabaseScheduler(DatabaseScheduler):
    def _default_now(self):
        return datetime.now(timezone.utc)