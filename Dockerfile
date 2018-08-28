ARG APP_PORT
FROM python:2.7-jessie

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN pip install -r requirements.txt
COPY . .

EXPOSE $APP_PORT
STOPSIGNAL SIGINT
CMD ["./run_gunicorn.sh", "staging"]