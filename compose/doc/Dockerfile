FROM python:3.7

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /doc

CMD python -m http.server 8000 --bind 0.0.0.0 --directory build/html
