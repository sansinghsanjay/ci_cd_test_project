pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "myapp:latest"
        CONTAINER_NAME = "myapp_container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sansinghsanjay/ci_cd_test_project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 8000:8000 $DOCKER_IMAGE'
            }
        }
    }
}
