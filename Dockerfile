FROM python:3.10.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DEBUG='false'

ENV RABBIT_HOST='35.199.70.141'
ENV RABBIT_PORT='5672'
ENV RABBIT_USERNAME='admin'
ENV RABBIT_PASSWORD='password@vascobank123'
ENV RABBIT_LOG_QUEUE='vascobank.logs'

ENV PAYMENY_API_HOST=''

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

RUN python manage.py migrate

EXPOSE 7003

CMD ["python", "-m", "guicorn", "--bind", "realstate.wsgi:application" ,"0.0.0.0:7003"]