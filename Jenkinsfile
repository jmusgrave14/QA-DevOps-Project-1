pipeline {
  agent any
  stages {
      stage('build') {
          sh "cd project1-python-flask"
          sh "sudo docker build -t localhost:8083/pythonapp ."
          sh "docker image ls"
      }
  }
}
