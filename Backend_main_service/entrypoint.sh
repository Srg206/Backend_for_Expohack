#!/bin/bash

# # Ожидание доступности базы данных
while ! pg_isready -q -h postgres -p ${POSTGRES_PORT} -U ${POSTGRES_USER}; do
  echo "$(date) - waiting for database to start"
  sleep 2
done
echo "$(date) - db started"

sleep 10
# Выполняем миграции
alembic upgrade head
alembic upgrade b61cfe201833
# Запускаем основное приложение
uvicorn main:app --host 0.0.0.0 --port 8000
exit 0
