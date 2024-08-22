pipeline {
    agent any
    
    stages {
      stage('Check Environment') {
            steps {
                sh 'docker --version'
                sh 'docker-compose --version'
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker-compose build web'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose run --rm web python -m pytest tests/'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    
    post {
        always {
            sh 'docker-compose down'
        }
    }
}