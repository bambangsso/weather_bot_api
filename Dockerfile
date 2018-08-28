ARG APP_PORT
FROM python:2.7-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./

RUN pip install -r requirements.txt
COPY . .

EXPOSE $APP_PORT
STOPSIGNAL SIGINT
CMD ["./run_gunicorn.sh", "staging"]