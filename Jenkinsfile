pipeline {
          agent {
              label 'BuildServer'
          }
          
          environment {
              // def img = ("${env.JOB_NAME}:${env.BUILD_ID}").toLowerCase()
              def registry = "gvenkat/flaskapp"
              def img = "${registry}" + ":${env.BUILD_ID}"
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

            		pyenv global pypy3.8-7.3.11'''
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

            stage('Running Coverage Metrics'){
              steps{
                  sh returnStatus: true, script: '''echo \'#### Run Coverage Metrics ####\'
                  source flaskapp/bin/activate
                  pytest --cov=main --cov-report xml'''
              }
              post {
                  success {
                    // One or more steps need to be included within each condition's block.
                    cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
                  }
              }
            }

            stage('Running Unit Test Cases'){
              steps{
                    sh returnStatus: true, script: '''echo \'#### Run Unit tests ####\'
                    source flaskapp/bin/activate
                    pytest utests --junitxml=./xmlReport/output.xml'''
              }
              post {
                success {
                  // One or more steps need to be included within each condition's block.
                  junit skipMarkingBuildUnstable: true, stdioRetention: '', testResults: 'xmlReport/output.xml'
                }
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
                            sh returnStatus: true, script: 'docker stop $(docker ps -a | grep ${env.registry} | awk \'{print $1}\')'
                            cont = docker.image("${img}").run("-p 5000:5000")
                            sleep (100)
                        }
                    }              
            }

            stage('Release') {
              steps {
                  echo 'Distribute Image to the Docker Hub'      
                  script {
                      docker.withRegistry('https://registry.docker.com','docker_registry'){
                          dockerImg.push()
                          dockerImg.push('latest')
                      }
                  }            
              }              
            } 
        }
}
