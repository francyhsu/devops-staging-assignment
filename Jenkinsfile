pipeline {
    agent { label 'testing' }
    
    environment {
        APP_VERSION = "1.0.${env.BUILD_NUMBER}"
        SONAR_TOKEN = "squ_d4470a13cff889e2b9b3ed747bab14d145ee3c93"
    }

    stages {
        stage('Source Integration') {
            steps {
                echo "Successfully triggered by GitHub Webhook."
            }
        }

        stage('Build and Package') {
            steps {
                echo "Cleaning and Packaging v${APP_VERSION}..."
                // Fix: Clean the build directory first to prevent recursion
                sh "rm -rf build && mkdir -p build"
                
                // Fix: Only zip relevant files (not the whole directory)
                sh "zip build/staging-app-v${APP_VERSION}.zip app.py schema.sql seed.sql load_test.js test_e2e.py"
                
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true
            }
        }

        stage('Code Quality (SonarQube)') {
            steps {
                echo "Running Static Analysis..."
                sh "sonar-scanner -Dsonar.projectKey=devops-staging-assignment -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.token=${SONAR_TOKEN}"
            }
        }

        stage('Database & Seeding') {
            steps {
                echo "Initializing Staging Database..."
                // Ensure your PostgreSQL Docker container is running!
                sh "docker exec -i staging-db psql -U postgres < schema.sql"
                sh "docker exec -i staging-db psql -U postgres < seed.sql"
            }
        }

        stage('Testing') {
            parallel {
                stage('Pytest E2E') {
                    steps {
                        // Ensure 'uvicorn app:app' is running in another terminal
                        sh "pytest test_e2e.py --html=report.html --self-contained-html"
                    }
                }
                stage('k6 Load Test') {
                    steps {
                        sh "k6 run load_test.js"
                    }
                }
            }
        }
    }

    post {
        success {
            mail to: 'hsufrancy2@gmail.com',
                 subject: "SUCCESS: Build #${env.BUILD_NUMBER} Completed",
                 body: "All 9 stages of the DevOps pipeline passed. Version ${APP_VERSION} is archived."
        }
        failure {
            mail to: 'hsufrancy2@gmail.com',
                 subject: "FAILURE: Build #${env.BUILD_NUMBER}",
                 body: "Pipeline failed. Check Jenkins logs for details."
        }
    }
}
