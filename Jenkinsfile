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

    stage('Run testRigor Tests (DEV)') {
      steps {
        withCredentials([string(credentialsId: 'testRigorToken', variable: 'TESTRIGOR_TOKEN')]) {
          sh '''
            echo "Triggering testRigor tests..."

            curl -X POST \
              -H "Content-Type: application/json" \
              -H "auth-token: $TESTRIGOR_TOKEN" \
              --data '{"forceCancelPreviousTesting":true}' \
              https://api.testrigor.com/api/v1/apps/DYnF8LHyZ83AeE7vv/retest

            echo "testRigor test triggered successfully"
          '''
        }
      }
    }
  }

  post {
    always { cleanWs() }
  }
}

