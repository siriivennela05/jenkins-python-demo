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
        
        stage('Run Python Script') {
            steps {
                script {
                    try {
                        sh 'python3 hello.py'
                    } catch (Exception e) {
                        echo "Python script execution failed, trying with python command"
                        sh 'python hello.py'
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
    }
    
    post {
        success {
            echo "Pipeline Job F completed successfully!"
        }
        failure {
            echo "Pipeline Job F failed!"
        }
    }
}
