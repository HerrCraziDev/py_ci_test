pipeline {
    agent any

    stages {
        stage("setup-env") {
            steps {
                sh """
                python3 -m venv env
                . env/bin/activate
                which pip
                pip install -r requirements.txt
                which pip
                """
            }
        }

        stage("linting") {
            steps {
                sh """
                . env/bin/activate
                flake8 tests greeter
                """
                sh """
                . env/bin/activate
                black tests greeter
                """
            }
        }

        stage("tests") {
            steps {
                sh """
                . env/bin/activate
                pytest --cov-report term-missing --cov-branch --cov greeter --junitxml=tests.xml
                """
            }
            
            post {
                always {
                    junit "tests.xml"
                }
            }
        }
    }
}
