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
        sh 'docker build -t mauolas/proyectocdk:1.0 .'
        sh 'docker images'
      }
    }

  }
}