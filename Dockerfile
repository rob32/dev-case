FROM python:3.10.5-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt ./requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

COPY . .
