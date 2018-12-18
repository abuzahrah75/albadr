FROM python:3.7

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8081

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8081