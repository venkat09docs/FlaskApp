def img = "httpd:2.4-alpine"
pipeline {
          agent {
              label 'BuildServer'
          }
          
          environment {
            container = ""
          }

          stages {
              stage('Run Docker') {
                  steps {
                      echo 'Running Httpd Container'
                      script {
                        container = docker.image("${img}").run("-d -p 80:80")
                      }
                  }
                  post {
                    always {
                        script {
                            if (container){
                                container.stop()
                            }
                        }
                    }
                  }
              }
          }
}
