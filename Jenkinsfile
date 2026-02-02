pipeline {
    agent { label 'testing' }
    stages {
        stage('Source Check') {
            steps {
                echo "Triggered automatically on branch: ${env.BRANCH_NAME}"
            }
        }
        stage('Main Branch Tasks') {
            when { branch 'main' } // Requirement: branch-specific behavior
            steps {
                echo "Running Staging environment deployment..."
            }
        }
        stage('Feature Branch Tasks') {
            when { not { branch 'main' } } 
            steps {
                echo "Running feature branch tests..."
            }
        }
    }
}
