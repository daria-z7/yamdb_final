FROM python:3.7-slim

# COPY ./ /app
WORKDIR /app

# COPY requirements.txt /app
COPY requirements.txt .

RUN pip3 install -r /app/requirements.txt --no-cache-dir 

# -- COPY api_yamdb/ /app

# WORKDIR /app/api_yamdb/
COPY . . 

# CMD ["python3", "manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
