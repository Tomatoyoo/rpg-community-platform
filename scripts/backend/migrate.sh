#!/bin/bash

# Применение миграций
alembic upgrade head

# Заполнение тестовыми данными
psql $DATABASE_URL -f seed_data.sql
