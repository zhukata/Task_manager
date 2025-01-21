FROM python:3.12

WORKDIR /

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./
COPY task_manager ./task_manager
COPY manage.py .

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && poetry install

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]