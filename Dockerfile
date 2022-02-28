FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y dnsutils

COPY DRipper2.py headers.txt /app/

WORKDIR /app
ENTRYPOINT ["python", "DRipper2.py"]
