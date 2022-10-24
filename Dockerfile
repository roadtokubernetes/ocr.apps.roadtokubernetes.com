FROM python:3.10.7-slim

COPY ./src /app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    tesseract-ocr \
    make \
    gcc

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install -r requirements.txt

RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN chmod +x config/entrypoint.sh

CMD [ "./config/entrypoint.sh" ]