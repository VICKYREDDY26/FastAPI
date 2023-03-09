pipeline {
  agent any
  stages {
    stage('Checkout-Code') {
      steps {
        git(url: 'https://github.com/VICKYREDDY26/FastAPI', branch: 'main', changelog: true)
      }
    }

    stage('shell-script') {
      steps {
        sh '''ls- la
'''
      }
    }

  }
}