pipeline {
  agent any
  stages {
    stage('Env&Tools') {
      steps {
        sh 'env'
        sh 'docker --version'
        sh 'ls -ltr'
      }
    }

    stage('DCKR Build') {
      steps {
        sh 'dockerImage= docker.build -t mauolas/proyectocdk:1.0 .'
        sh 'docker images'
      }
    }

    stage('Deploy image') {
      steps {
        sh 'docker push mauolas/proyectocdk:1.0'
      }
    }

  }
  environment {
    registryCrendencial = 'dockerhub_id'
    dockerimage = ''
  }
}