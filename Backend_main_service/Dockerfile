# Указываем базовый образ
FROM python:3.9-slim

# Устанавливаем необходимые пакеты
RUN apt-get update && \
    apt-get install -y libpq-dev gcc postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Устанавливаем зависимости
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем код приложения
COPY . /app

# Копируем entrypoint файл
COPY ./entrypoint.sh /app/entrypoint.sh

# Устанавливаем права на выполнение для entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Указываем рабочую директорию
WORKDIR /app

# Команда по умолчанию
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
