pipeline {
    agent { label 'testing' }
    
    environment {
        // Semantic Versioning for Question 4
        APP_VERSION = "1.0.${env.BUILD_NUMBER}"
        // Token for Question 5
        SONAR_TOKEN = "PASTE_YOUR_SONAR_TOKEN_HERE"
    }

    stages {
        stage('Source Integration') {
            steps {
                echo "Successfully triggered by GitHub Webhook."
                echo "Branch: ${env.BRANCH_NAME}"
            }
        }

        stage('Build and Package') {
            steps {
                echo "Packaging v${APP_VERSION}..."
                sh "mkdir -p build"
                // Include app.py and schema.sql in the artifact
                sh "zip -r build/staging-app-v${APP_VERSION}.zip . -x '*.git*'"
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
            }
        }

        stage('Code Quality (SonarQube)') {
            steps {
                echo "Running Static Analysis..."
                sh "sonar-scanner -Dsonar.projectKey=devops-staging-assignment -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=${SONAR_TOKEN}"
            }
        }

        stage('Database & Seeding') {
            steps {
                echo "Initializing Staging Database..."
                // Run schema and seed scripts against Docker container (Question 6)
                sh "docker exec -i staging-db psql -U postgres < schema.sql"
                sh "docker exec -i staging-db psql -U postgres < seed.sql"
            }
        }

        stage('E2E & Performance Testing') {
            parallel {
                stage('Pytest E2E') {
                    steps {
                        echo "Running User Journey Tests..."
                        sh "pytest test_e2e.py --html=report.html --self-contained-html"
                    }
                }
                stage('k6 Load Test') {
                    steps {
                        echo "Running Performance Stress Test..."
                        sh "k6 run load_test.js"
                    }
                }
            }
        }
    }

    post {
        success {
            // Notification for Question 9
            mail to: 'your-email@uchicago.edu',
                 subject: "SUCCESS: Build #${env.BUILD_NUMBER} Deployed",
                 body: "Staging pipeline completed successfully. Version ${APP_VERSION} is ready."
        }
        failure {
            // Notification for Question 9
            mail to: 'your-email@uchicago.edu',
                 subject: "FAILURE: Build #${env.BUILD_NUMBER}",
                 body: "The pipeline failed at stage ${env.STAGE_NAME}. Check logs at ${env.BUILD_URL}"
        }
    }
}
// Final Deployment Test
