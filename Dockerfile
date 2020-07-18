FROM python:3.8-buster as builder

WORKDIR /opt/app/weather-store

COPY requirements.lock /opt/app/weather-store
RUN pip install -r requirements.lock

FROM python:3.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

COPY app /opt/app/weather-store

WORKDIR /opt/app/weather-store
