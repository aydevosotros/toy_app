FROM python:3.8

RUN apt-get update && apt-get install -y \
    libmysqlclient
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/app
COPY toy_app /opt/app
WORKDIR /opt/app
COPY requirements.txt /opt/app/.
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:80


