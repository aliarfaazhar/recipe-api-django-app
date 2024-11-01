FROM python:3.10-slim
LABEL maintainer="aliarfaazhar"

ENV PYTHONBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client build-essential libpq-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get purge -y --auto-remove build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/* /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user
    
ENV PATH="/py/bin:$PATH"

USER django-user
