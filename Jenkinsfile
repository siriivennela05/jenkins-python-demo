pipeline {
    agent {
        label 'docker-agent'
    }
    
    stages {
        stage('Information') {
            steps {
                echo "NAME: Siri Vennela"
                echo "ROLL NUMBER: Se22ucse212"
                echo "Running on node: ${env.NODE_NAME}"
            }
        }
        
        stage('Docker Info') {
            steps {
                sh '''
                echo "Host information:"
                hostname
                uname -a | head -n 1
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
