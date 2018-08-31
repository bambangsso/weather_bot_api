if [ $# -ne 1 ]; then
   echo "Usage: ./build-docker-app.sh <docker name>"
   exit 1
fi

DOCKER_REPO_NAME=`echo $1 | awk '{print tolower($0)}'`
APP_PORT=`grep App_Port Conf.Staging.json | awk -F':' '{print $2}'`

APP_PORT=`echo $APP_PORT | sed 's/[^0-9]*//g'`
if [[ $APP_PORT = *[[:digit:]]* ]]; then
   echo "Found application port $APP_PORT, building docker"

   CONTAINER_ID=`sudo docker ps -q --filter ancestor=$DOCKER_REPO_NAME`
   sudo docker ps -q --filter ancestor=$DOCKER_REPO_NAME
   echo "Container ID: $CONTAINER_ID"
   if [ ${#CONTAINER_ID} -gt 0 ]; then
      echo "$DOCKER_REPO_NAME is running with container id: $CONTAINER_ID, shut it down"
      sudo docker kill $CONTAINER_ID
   fi
   sleep 5

   sudo docker build --build-arg APP_PORT=$APP_PORT -t $DOCKER_REPO_NAME .
   sleep 5
   sudo docker run -d -p $APP_PORT:$APP_PORT $DOCKER_REPO_NAME --name $DOCKER_REPO_NAME
   sleep 5
else
   echo "Application port is not found, you need to define on the Conf.Staging.json file. Docker build terminated"
fi
