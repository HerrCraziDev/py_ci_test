pipeline {
    agent any

    stages {
        stage("setup-env") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage("linting") {
            steps {
                sh 'flake8 tests greeter'
                sh 'black tests greeter'
            }
        }

        stage("tests") {
            steps {
                sh 'pytest --cov-report term-missing --cov-branch --cov greeter'
            }
        }
    }
}