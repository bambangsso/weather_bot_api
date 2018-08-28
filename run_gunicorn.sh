#!/bin/sh
if [ $# -ne 1 ]; then
   echo "Usage: ./run_gunicorn.sh <dev|staging|prod>"
   exit 1
fi
export RUN_AS=$1 

APP_PORT=`grep App_Port Conf.Staging.json | awk -F':' '{print $2}'`
APP_PORT=`echo $APP_PORT | sed 's/[^0-9]*//g'`
if [ ${#APP_PORT} -gt 0 ]; then
   echo "Found application port $APP_PORT, building docker"
   gunicorn server_call_weather_api:app --workers=1 --bind=0.0.0.0:$APP_PORT --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
else
   echo "Application port is not found, you need to define on the Conf.Staging.json file. Docker build terminated"
fi