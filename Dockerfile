FROM python:3.9

WORKDIR /news-classifier

COPY . /news-classifier/

WORKDIR /news-classifier/server

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /news-classifier/server/app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]