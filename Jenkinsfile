pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        sh '''
          python3 -V
          python3 -m pip install --upgrade pip
          pip3 install -r requirements.txt
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest -q'
      }
    }
  }
}
