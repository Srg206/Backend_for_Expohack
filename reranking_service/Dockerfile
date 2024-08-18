FROM python:3.9-slim

# Устанавливаем необходимые зависимости
COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y libpq-dev gcc postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

# Копируем код проекта в контейнер
COPY . .

# Запускаем скрипт
CMD ["python", "main.py"]
