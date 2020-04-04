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
      parallel {
        stage('Dckr instru') {
          steps {
            sh 'echo \'docker build -t mauolas/proyectoCDK:1.0\''
          }
        }

        stage('DCKR Build') {
          steps {
            sh 'docker build -t mauolas/proyectocdk:1.0 .'
          }
        }

        stage('Docker images') {
          steps {
            sh 'docker images'
          }
        }

      }
    }

  }
}