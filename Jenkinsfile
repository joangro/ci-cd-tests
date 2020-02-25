pipeline {
    agent any
    stages {
        stage('test-python') {
            steps {
                agent { docker { image 'python:3.5.1' } }
                sh 'python --version'
            }
        }
        stage('build-app') {
            steps {
                sh 'docker build -t my-ci-app:latest'
            }
        }
        stage('test-app') {
            steps {
                sh 'docker run -p 8080:8080 my-ci-app:latest'
            }
        }
    }
}
