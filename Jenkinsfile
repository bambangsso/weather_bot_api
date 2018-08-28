//This script is created by BJtech DevOps copyright August 2018 (c)

pipeline {
  agent any

  stages {

    stage('Upload APP to staging') {
      steps {
	sh 'ssh jenkins@10.140.0.22 "rm -fR ${JOB_NAME} && mkdir ${JOB_NAME}"'
	sh 'scp -r . jenkins@10.140.0.22:/home/jenkins/${JOB_NAME}'
      }
    }

    stage('Dockerizing APP') {
      steps {
	sh 'ssh jenkins@10.140.0.22 "cd /home/jenkins/${JOB_NAME} && ./build-docker-app.sh ${JOB_NAME}"'
      }
    }


    stage('UI Test') {
      steps {
	sh 'curl http://10.140.0.22:3002/checkHello'
      }
    }

    stage('Integration Test') {
      steps {
        echo 'skipping selenium test'
      }
    }

  }

}