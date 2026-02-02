// Trigger Build #4
pipeline {
    agent { label 'testing' } 
    stages {
        stage('Initial Build') {
            steps {
                echo "Running on branch: ${env.BRANCH_NAME}"
            }
        }
        stage('Feature Branch Tasks') {
            when { not { branch 'main' } } 
            steps {
                echo "Executing experimental feature tests..."
            }
        }
        stage('Main Branch Staging') {
            when { branch 'main' } 
            steps {
                echo "Executing production-ready staging deployment..."
            }
        }
    }
}
