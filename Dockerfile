FROM python:3.9.4-slim

RUN apt-get update && apt-get install -y netcat

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["./prestart.sh"]
