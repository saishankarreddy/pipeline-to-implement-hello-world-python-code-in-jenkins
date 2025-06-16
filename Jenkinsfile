// Jenkinsfile

pipeline {
    // Defines where the pipeline will run. 'any' means any available agent.
    // For more control, you could specify: agent { label 'my-python-agent' }
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // This step typically checks out your source code from Git.
                // Jenkins automatically handles this if the SCM (Source Code Management)
                // is configured in your job. We include it here for clarity.
                checkout scm
                echo "Code checked out successfully."
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    echo "Executing hello_world.py..."
                    // Use 'sh' for shell commands (Linux/macOS) or 'bat' for Windows batch commands.
                    // This assumes Python is installed and accessible in the Jenkins agent's PATH.
                    sh 'python hello_world.py'
                    echo "Python script finished (no arguments)."

                    echo "Executing hello_world.py with an argument..."
                    sh 'python hello_world.py JenkinsUser'
                    echo "Python script finished (with argument)."
                }
            }
        }
    }

    // Post-build actions (optional but good practice)
    post {
        always {
            echo "Pipeline finished. Status: ${currentBuild.result}"
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check console output for details."
        }
    }
}
