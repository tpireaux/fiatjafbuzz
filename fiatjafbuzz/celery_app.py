from celery import Celery
from celery.schedules import crontab
from fiatjafbuzz.settings import Settings

settings = Settings()

celery_app = Celery(
    "fiatjafbuzz",
    broker=settings.redis_broker_url,
    backend=settings.redis_backend_url,
    include=["fiatjafbuzz.tasks"],
)

celery_app.conf.timezone = "America/New_York"
celery_app.conf.enable_utc = False

celery_app.conf.beat_schedule = {
    "run-bot-every-day": {
        "task": "fiatjafbuzz.tasks.run_bot",
        "schedule": crontab(hour=settings.cron_hours, minute=settings.cron_minutes),
    },
}
