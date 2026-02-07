pipeline {
  agent any

  environment {
    // Make sure Jenkins can find Homebrew Python + common paths
    PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:${env.PATH}"
  }

  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup Python') {
      steps {
        sh '''
          which python3 || true
          python3 -V
          python3 -m venv .venv
          . .venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run Tests') {
      steps {
        sh '''
          . .venv/bin/activate
          pytest -q
        '''
      }
    }
  }

  post {
    always { cleanWs() }
  }
}
