FROM python:3.9

RUN pip3 install flask gunicorn

COPY . .
EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
