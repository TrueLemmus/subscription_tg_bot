# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY bot/requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем исходный код бота
COPY bot/ .

# Копируем .env файл
COPY .env .env

# Указываем переменные окружения по умолчанию (можно переопределить в docker-compose.yml)
ENV CELERY_BROKER=redis://redis:6379/0
ENV CELERY_BACKEND=redis://redis:6379/0

# Команда по умолчанию (может быть переопределена в docker-compose.yml)
CMD ["python", "main.py"]