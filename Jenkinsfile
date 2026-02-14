pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Setup venv + Install deps') {
      steps {
        sh '''
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
}
