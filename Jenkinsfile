pipeline {
  agent {
    docker { image 'python:3.11-slim' }
  }

  stages {
    stage('Setup Python') {
      steps {
        sh 'python -V'
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          pip install --upgrade pip
          pip install -r requirements.txt
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
