FROM --platform=linux/amd64 python:3.9

EXPOSE 8000

WORKDIR /app

COPY . /app

RUN python -m venv /app/venv && \
    . /app/venv/bin/activate && \
    /app/venv/bin/python -m ensurepip && \
    /app/venv/bin/python -m pip install --upgrade pip && \
    /app/venv/bin/python -m pip install --no-cache-dir -r /app/requirements.txt && \
    apt-get update && \
    apt-get install -y dos2unix && \
    apt-get clean && \
    dos2unix /app/bin/*.sh && \
    chmod a+x /app/bin/*.sh && \
    /app/src/manage.py collectstatic -c --noinput

ENV PATH="/app/venv/bin:/app/bin:$PATH"

CMD start.sh
