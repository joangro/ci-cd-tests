pipeline {
    agent any
    stages {
        stage('test-python') {
            steps {
                sh 'python --version && ls -lFa && pwd'
            }
        }
        stage('build-app') {
            steps {
                sh 'docker build -t my-ci-app:latest .'
            }
        }
        stage('test-build') {
            steps {
                sh 'export CONTAINER_ID=$(docker run -d --rm -p 8081:8080 my-ci-app:latest)'
                sh '''
                sleep 2
                export RESPONSE_CODE=$(curl -s -o /dev/null -w "%{http_code}" localhost:8081)
                echo $RESPONSE_CODE | python -c "import sys;assert str(next(sys.stdin)).strip()=='200', 'Code received is different than 200 OK!'"
                '''

            }
        }
    }
}
