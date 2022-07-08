FROM python:3.7-slim

COPY ./ /app

# COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt

# COPY api_yamdb/ /app

WORKDIR /app/api_yamdb/

# CMD ["python3", "manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"]
