pipeline {
    agent { label 'testing' }
    stages {
        stage('Source Integration') {
            steps {
                echo "Triggered by GitHub on branch: ${env.BRANCH_NAME}"
            }
        }
        stage('Feature Testing') {
            when { not { branch 'main' } } // Runs only for non-main branches
            steps {
                echo "Experimental feature testing in progress..."
            }
        }
        stage('Staging Quality Check') {
            when { branch 'main' } // Runs only for the main branch
            steps {
                echo "Running production-ready checks for Staging..."
            }
        }
    }
}
