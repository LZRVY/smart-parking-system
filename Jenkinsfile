pipeline {
    agent any

    environment {
        APP_NAME = "smart-parking-app"
        CONTAINER_NAME = "smart-parking-dev"
        PUBLIC_URL = "http://13.58.211.204"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${APP_NAME}:dev .
                """
            }
        }

        stage('Deploy to DEV') {
            steps {
                sh """
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 80:5000 ${APP_NAME}:dev
                """
            }
        }

       stage('Trigger testRigor') {
  steps {
    withCredentials([string(credentialsId: 'TESTRIGOR_TOKEN', variable: 'TESTRIGOR_TOKEN')]) {
      sh '''
        set -e
        echo "Triggering testRigor..."
        curl -sS -X POST \
          -H "Content-Type: application/json" \
          -H "auth-token: $TESTRIGOR_TOKEN" \
          --data '{"forceCancelPreviousTesting":true}' \
          https://api.testrigor.com/api/v1/apps/DYnF8LHyZ83AeE7vv/retest
        echo ""
        echo "testRigor triggered."
      '''
    }
  }
}
    
}

    post {
        always {
            echo "========================================"
            echo "Application is live at: ${PUBLIC_URL}"
            echo "========================================"
        }
    }
}
