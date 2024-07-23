pipeline {
          agent {
              label 'BuildServer'
          }
          
          environment {
              def img = ("${env.JOB_NAME}:${env.BUILD_ID}").toLowerCase()
          }

          stages {
              stage('Checkout Code') {
                        steps {
                            echo 'Checkout Code'
                            git 'https://github.com/venkat09docs/FlaskApp.git'
                            sh 'ls -l'
                        }              
               }
               stage('Build Image') {
                        steps {
                            echo 'Build Docker Image using Docker file'
                            // docker build -t flaskapp:v1 .
                            script { 
                              dockerImg = docker.build("${img}")
                            }
                }              
          }
          }
}
