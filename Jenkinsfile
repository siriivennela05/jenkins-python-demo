pipeline {
    agent {
        label 'docker-agent'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code from Git repository"
                checkout scm
            }
        }
        
        stage('Information') {
            steps {
                echo "Running Pipeline Job F from Jenkinsfile in Git"
                echo "NAME: Siri Vennela"
                echo "ROLL NUMBER: Se22ucse212"
                echo "Running on node: ${env.NODE_NAME}"
            }
        }
        
        stage('Environment') {
            steps {
                echo "Environment Variables:"
                sh 'env | sort'
            }
        }
        
        stage('List Repository Contents') {
            steps {
                sh 'ls -la'
                sh 'pwd'
            }
        }
        
        stage('Python Check') {
            steps {
                script {
                    echo "Checking if Python is available..."
                    def pythonExists = sh(script: "command -v python3 || command -v python || echo 'not found'", returnStdout: true).trim()
                    
                    if (pythonExists.contains("not found")) {
                        echo "Python is not installed on this agent. Skipping Python execution."
                    } else {
                        echo "Python is available at: ${pythonExists}"
                        try {
                            if (pythonExists.contains("python3")) {
                                sh "python3 hello.py"
                            } else {
                                sh "python hello.py"
                            }
                        } catch (Exception e) {
                            echo "Python script execution failed, but continuing with pipeline."
                            echo "Error: ${e.message}"
                        }
                    }
                }
            }
        }
        
        stage('Create Output File') {
            steps {
                sh '''
                echo "Creating jenkinsfile_output.txt file..."
                echo "This file was created by Jenkins Pipeline Job F using Jenkinsfile from Git" > jenkinsfile_output.txt
                echo "Repository contents:" >> jenkinsfile_output.txt
                ls -la >> jenkinsfile_output.txt
                echo "File created successfully"
                cat jenkinsfile_output.txt
                '''
            }
        }
        
        stage('Docker Info') {
            steps {
                sh '''
                echo "Host information:"
                hostname
                uname -a
                '''
            }
        }
    }
    
    post {
        success {
            echo "Pipeline Job F completed successfully!"
        }
        failure {
            echo "Pipeline Job F failed!"
        }
        always {
            echo "Pipeline execution completed at $(date)"
        }
    }
}
