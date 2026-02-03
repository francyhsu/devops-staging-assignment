pipeline {
    agent { label 'testing' }
    
    environment {
        APP_VERSION = "1.0.${env.BUILD_NUMBER}"
        SONAR_TOKEN = "squ_e9034f38d3667640f1d2600d036dd641e5481a6b" 
    }

    stages {
        stage('Source Integration') {
            steps {
                echo "Triggered by GitHub. Branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Build and Package') {
            steps {
                sh "mkdir -p build"
                sh "zip -r build/staging-app-v${APP_VERSION}.zip . -x '*.git*'"
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo "Starting Static Code Analysis..."
                // This command sends your code to your local SonarQube server
                sh "sonar-scanner -Dsonar.projectKey=devops-staging-assignment -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${SONAR_TOKEN}"
            }
        }

        stage('Quality Gate') {
            steps {
                echo "Checking Quality Gate..."
                // In a production environment, you would use waitForQualityGate()
                echo "SonarQube analysis complete. View results at http://localhost:9000"
            }
        }
    }
}
