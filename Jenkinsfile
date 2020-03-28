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

    stage('Build DCKR') {
      steps {
        sh 'echo \'docker build -t mauolas/proyectoCDK:1.0\''
      }
    }

  }
}