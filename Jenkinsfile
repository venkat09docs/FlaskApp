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

            stage('Py Env Preparation'){
        	   steps{
            		sh '''#!/bin/bash
            		source ~/.bashrc
            		pyenv versions

            		pyenv global 3.10.0'''
        	   }
  	        }

            stage('Py Venv Setup'){
              steps{
                sh '''echo "#### Create venv and activate it python version 3.10.0 ####"
                python3 -m venv flaskapp
                source flaskapp/bin/activate
                python3 -V

                echo "##### Install required Python Modules ####"
                pip install -r requirements.txt

                # Cobertura - Code Coverage
                pip install coverage
                pip install pytest-cov'''
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

            stage('Deploy Container') {
                    steps {
                        echo 'Deploy Container'
                        script { 
                            cont = docker.image("${img}").run("-d -p 5000:5000")
                            sleep (100)
                        }
                    }              
            }
        }
}
