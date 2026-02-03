pipeline { 
    agent { label 'testing' } 
    environment { 
        // Requirement: Semantic versioning using build numbers
        APP_VERSION = "1.0.${env.BUILD_NUMBER}" 
    } 
    stages { 
        stage('Source Integration') { 
            steps { 
                echo "Triggered by GitHub. Branch: ${env.BRANCH_NAME}" 
            } 
        } 
        stage('Build and Package') { 
            steps { 
                echo "Packaging Application v${env.APP_VERSION}..." 
                // 1. Create a clean build directory 
                sh "mkdir -p build" 
                // 2. Prepare the artifacts (App code and Database schema) 
                sh "cp app.py schema.sql build/" 
                // 3. Package into a versioned ZIP file (Semantic Versioning) 
                sh "zip -r build/staging-app-v${env.APP_VERSION}.zip build/" 
                // 4. Requirement: Store artifacts in Jenkins
                archiveArtifacts artifacts: 'build/*.zip', fingerprint: true 
            } 
        } 
        stage('Branch Specific Tasks') { 
            steps { 
                script { 
                    if(env.BRANCH_NAME == 'main') { 
                        echo "Main branch detected: Preparing for Staging Deployment." 
                    } else { 
                        echo "Feature branch detected: Running experimental tests." 
                    } 
                } 
            } 
        } 
    } 
    post { 
        success { 
            echo "Successfully built and archived version ${env.APP_VERSION}" 
        } 
    } 
}
