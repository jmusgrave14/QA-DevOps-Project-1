pipeline {
  agent any
  environment {
      NEXUS_LOGIN=credentials('NEXUS_LOGIN')
  }
  stages {
      stage('build') {
        steps (
          sh "sudo docker build -t localhost:8083/pythonapp ."
        )
      }
      stage('push') (
        steps (
          sh "sudo docker login localhost:8083 -u ${NEXUS_LOGIN_USR} -P ${NEXUS_LOGIN_PSW}"
  }
}
