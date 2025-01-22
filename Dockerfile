FROM python:3.12

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY task_manager ./task_manager
COPY manage.py .

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
