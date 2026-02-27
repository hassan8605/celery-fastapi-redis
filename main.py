from fastapi import FastAPI
from celery.result import AsyncResult
from celery_app import celery_app
from utils import add_numbers_task
import uvicorn
app = FastAPI(title="FastAPI + Celery Demo")


@app.post("/add")
async def add_numbers(a: int, b: int):
    """
    Sends addition task to Celery
    """
    task = add_numbers_task.delay(a, b)

    return {
        "message": "Task sent to Celery",
        "task_id": task.id
    }


@app.get("/result/{task_id}")
async def get_result(task_id: str):
    """
    Check task result from Redis
    """
    task_result = AsyncResult(task_id, app=celery_app)

    if task_result.state == "PENDING":
        return {"status": "PENDING"}

    if task_result.state == "SUCCESS":
        return {
            "status": "SUCCESS",
            "result": task_result.result
        }

    if task_result.state == "FAILURE":
        return {
            "status": "FAILURE",
            "error": str(task_result.result)
        }

    return {"status": task_result.state}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5245)