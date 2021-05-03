FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# ENV DATABASE_URL 'postgresql://postgres:'

# set working directory
WORKDIR /app

# copy dependencies
COPY requirements.txt /app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /app/
