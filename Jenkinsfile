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

  post {
     always {
        echo 'Sending email SUCCESS or FAILED'

        sh "curl -i -X GET 'https://api.telegram.org/bot663264986:AAH2cQ8bgVdkslwG9jGwEAmJZ2nt--baO4A/sendMessage?chat_id=139934550&text=Hi%20BJtech%20tim,%20aku%20infoin%20ada%20proses%20integrasi%20dan%20deployement%20task%20${env.JOB_NAME}%20dgn%20status%20${env.BUILD_STATUS}.%20Untuk%20keterangan%20lebih%20jelas%20kunjungi%20${env.BUILD_URL}'"
            
        emailext body: "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
           recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
           subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
           to: 'bambang.sso@gmail.com, rizky@bangjoni.com'
            
     }
  }

}