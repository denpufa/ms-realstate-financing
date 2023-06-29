FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

RUN python manage.py migrate

EXPOSE 7003

CMD ["python", "-m", "guicorn", "--bind", "realstate.wsgi:application" ,"0.0.0.0:7003"]