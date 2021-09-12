pipeline {
  agent any
  stages {
    stage('setup-env') {
      steps {
        sh 'python3 -m venv env'
        sh '. env/bin/activate'
        sh 'pip install -r requirements.txt'
        sh '''which pip
'''
      }
    }

    stage('linting') {
      steps {
        sh 'flake8 tests greeter'
        sh 'black tests greeter'
      }
    }

    stage('tests') {
      steps {
        sh 'pytest --cov-report term-missing --cov-branch --cov greeter'
      }
    }

  }
}