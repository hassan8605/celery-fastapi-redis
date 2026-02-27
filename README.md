# Celery with Redis Walkthrough

This project demonstrates how to use Celery with Redis to perform background tasks in a Python application. The example showcases a simple math service with a Celery task.

## 📦 Requirements

- Python 3.8+
- Redis server running locally or accessible over network
- Packages defined in `requirements.txt` (Celery, Redis, FastAPI if used)

## 🔧 Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Redis**
   Ensure Redis is running. On Windows you can use WSL or a Docker container:
   ```bash
   redis-server
   ```

3. **Run the Celery worker**
   From the project root directory:
   ```bash
   celery -A celery_app.celery_app worker --loglevel=info
   ```

4. **Trigger tasks**
   Import and call the task from your application code:
   ```python
   from utils import add_numbers_task

   result = add_numbers_task.delay(2, 3)
   print(result.get())  # should output 5 after the task completes
   ```

## 🧠 How It Works

- `celery_app.py` configures the Celery instance, pointing it to the Redis broker.
- `utils.py` defines a heavy computation (`MathService.add`) and wraps it as a Celery task using the `@celery_app.task` decorator.
- The task can be called asynchronously with `.delay()` and the result is fetched using `.get()`.

## 📚 Further Reading

For a more comprehensive explanation and step-by-step guide, check out my Medium article:

> Running background tasks in FastAPI using Celery and Redis: a practical guide
> https://medium.com/@hassan.mahmood1/running-background-tasks-in-fastapi-using-celery-and-redis-a-practical-guide-813545cf81f8

This article covers configuration, example code, and deployment tips.

---

Feel free to explore and modify the tasks to suit your own use case. Happy coding! 🎉
