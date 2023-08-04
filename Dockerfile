FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY tests_ndvi .

ENV API_GATEWAY_URL="https://eoapi-dev.thaicom.io/main/collections/sentinel-2-l2a-ndvi"
ENV POLYGON="POLYGON ((99.6396462 14.9847325, 99.6393786 14.9847605, 99.637582 14.985196, 99.6377248 14.9855344, 99.6378874 14.9854322, 99.6384408 14.9854274, 99.6390221 14.9853392, 99.640132 14.985232, 99.6396462 14.9847325))"
ENV X_API_KEY="pXSZunw7R819HN8CtZZm05FbHzNrYV5i7cTuUPCT"
ENV PYTHONPATH="app"

CMD ["python", "-m", "pytest", "conftest.py", "-vv", "-o", "log_cli=true", "--html=report.html"]
