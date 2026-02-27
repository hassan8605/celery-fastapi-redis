from celery import Celery

class CeleryConfig:
    BROKER_URL = "redis://localhost:6379/0"
    RESULT_BACKEND = "redis://localhost:6379/0"

def make_celery() -> Celery:
    celery = Celery(
        "worker",
        broker=CeleryConfig.BROKER_URL,
        backend=CeleryConfig.RESULT_BACKEND,
    )

    celery.conf.update(
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        timezone="UTC",
        enable_utc=True,
    )

    return celery

celery_app = make_celery()
import utils