pipeline {
  agent any

  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build + Test in Docker') {
      steps {
        sh '''
          docker version
          docker build -t smart-parking-app:dev .
          docker run --rm smart-parking-app:dev python -m pytest -q
        '''
      }
    }

    stage('Deploy to Dev') {
      steps {
        sh '''
          echo "Deploying to DEV environment..."
          docker rm -f smart-parking-dev || true
          docker run -d --name smart-parking-dev -p 5001:5000 smart-parking-app:dev
          echo "DEV running on http://localhost:5001"
        '''
      }
    }
  }

  post {
    always { cleanWs() }
  }
}

