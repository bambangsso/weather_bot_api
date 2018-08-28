import os
import json

RUN_AS = os.getenv('RUN_AS', 0)

if (RUN_AS == "dev"):
   fileConfig = "Conf.Development.json"
elif (RUN_AS == "staging"):
   fileConfig = "Conf.Staging.json"
elif (RUN_AS == "prod"):
   fileConfig = "Conf.Production.json"
else:
   fileConfig = "None"

if (fileConfig != "None"):
   with open(fileConfig) as json_file:
      data = json.load(json_file)

   MySQL_Host = data['MySQL_Host']
   MySQL_Port = data['MySQL_Port']
   MySQL_User = data['MySQL_User']
   MySQL_Password = data['MySQL_Password']
   MySQL_Database = data['MySQL_Database']
   MySQL_Debug = data['MySQL_Debug']
   MySQL_ConLimit = data['MySQL_ConLimit']
   Redis_Host = data['Redis_Host']
   Redis_Port = data['Redis_Port']
   S3_ACCESS_KEY = data['S3_ACCESS_KEY']
   S3_SECRET_KEY = data['S3_SECRET_KEY']
   S3_POOL_SIZE = data['S3_POOL_SIZE']
   USER_VAR_TIMEOUT = data['USER_VAR_TIMEOUT']
   SMTP_HOST = data['SMTP_HOST']
   SMTP_PORT = data['SMTP_PORT']
   SMTP_USER = data['SMTP_USER']
   SMTP_PASSWORD = data['SMTP_PASSWORD']
   LIVEAGENT_HOST = data['LIVEAGENT_HOST']
   LIVEAGENT_PORT = data['LIVEAGENT_PORT']   
   App_Port = data['App_Port']
