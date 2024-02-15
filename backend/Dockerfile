# Official Python parent image
FROM python:3.9-slim

#Set environment variables
# PYTHONUNBUFFERED - prevents python from buffering stdout and stderr
# PYTHONDONTWRITEBYTECODE - Prevents python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Sets the Working Directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project
COPY . /code/

# Runs the applciation on container start up
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo.wsgi:application"]