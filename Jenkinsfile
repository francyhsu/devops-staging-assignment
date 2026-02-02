pipeline {
    agent { label 'testing' } 
    
    // This allows the build to trigger even if there's a minor environmental delay
    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('Source Integration') {
            steps {
                echo "Successfully triggered by GitHub Webhook."
                echo "Current Build Branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Feature Branch Tasks') {
            when { 
                not { branch 'main' } 
            } 
            steps {
                echo "DEBUG: Non-main branch detected (${env.BRANCH_NAME})."
                echo "Executing experimental feature tests for development..."
            }
        }

        stage('Main Branch Staging') {
            when { 
                branch 'main' 
            } 
            steps {
                echo "DEBUG: Main branch detected."
                echo "Executing production-ready staging deployment tasks..."
            }
        }
    }

    post {
        always {
            echo "Pipeline execution finished on ${env.NODE_NAME}."
        }
    }
}
