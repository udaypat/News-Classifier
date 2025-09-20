FROM python:3.9-alpine


ENV UV_SYSTEM_PYTHON=1

WORKDIR /news-classifier


COPY . /news-classifier/

WORKDIR /news-classifier/server


RUN apk add --no-cache \
    build-base \
    gfortran \
    lapack-dev \
    blas-dev \
    linux-headers \
    curl \
    ca-certificates

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

ENV PATH="/root/.local/bin/:$PATH"


COPY server/requirements.txt ./server/requirements.txt

RUN uv pip install --system -r server/requirements.txt

COPY . .


WORKDIR /news-classifier/server/app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
