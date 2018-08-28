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

   App_Port = data['App_Port']
