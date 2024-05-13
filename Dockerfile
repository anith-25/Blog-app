FROM python:3.10-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements/requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/