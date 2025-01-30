FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    pkg-config \
    libffi-dev \
    libssl-dev \
    libsecp256k1-dev \
 && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.5.1
ENV TZ=America/New_York

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock .env ./

RUN poetry install --only main --no-interaction --no-ansi

COPY fiatjafbuzz fiatjafbuzz
COPY run-now.sh /usr/local/bin/run-now.sh
RUN chmod +x /usr/local/bin/run-now.sh

EXPOSE 5555