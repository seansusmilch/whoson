FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update && apt upgrade -y && pip install --no-cache-dir -r requirements.txt

COPY ./bot.py .
COPY ./prod.py .
COPY ./web.py .

VOLUME ["/config"]

CMD ["python", "./prod.py"]