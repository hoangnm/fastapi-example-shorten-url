#!/bin/bash
while !</dev/tcp/db/5432; do sleep 1; done;
alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --reload
