from celery_app import celery_app
import time

class MathService:
    @staticmethod
    def add(a: int, b: int) -> int:
        # simulate heavy work
        time.sleep(3)
        return a + b


@celery_app.task(name="add_numbers_task")
def add_numbers_task(a: int, b: int) -> int:
    return MathService.add(a, b)
