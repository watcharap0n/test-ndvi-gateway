FROM python:3.10-slim

WORKDIR test-ndvi-gateway

COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY tests_ndvi .

WORKDIR ../

CMD ["pytest", "tests_ndvi/conftest.py", "-vv", "-o", "log_cli=true", "--html=report.html"]
