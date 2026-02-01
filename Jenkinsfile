pipeline {
    agent none 
    stages {
        stage('Unit Testing') {
            agent { label 'testing' } 
            steps {
                echo 'Running tests on the MacBook Agent...'
                sh 'python3 --version' 
            }
        }
        stage('Staging Deployment') {
            agent { label 'deployment' }
            steps {
                echo 'Deploying to Staging...'
            }
        }
    }
}
