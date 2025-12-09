pipeline {
    agent any

    stages {

        stage('Debug Environment') {
            steps {
                bat 'echo Current user: %USERNAME%'
                bat 'where cmd'
                bat 'echo %PATH%'
            }
        }

        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install') {
            steps {
                withEnv([
                    "PATH=C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\Wbem;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                ]) {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Pull Data/Model') {
            steps {
                withEnv([
                    "PATH=C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\Wbem;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                ]) {
                    bat 'dvc pull'
                }
            }
        }
        
        stage('Test') {
            steps {
                withEnv([
                    "PATH=C:\\Windows\\System32;C:\\Windows;C:\\Windows\\System32\\Wbem;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313;" +
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                ]) {
                    bat "pip show pytest"
                    bat "where pytest"
                    bat 'python -m pytest'
                }
            }
        }
        
        stage('Build Docker') {
            steps {
                bat 'docker build -t housing-model-api .'
            }
        }
        /*
        stage('Push Docker') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-pass',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {

                    bat """
                    echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                    docker tag housing-model-api %DOCKER_USERNAME%/housing-model-api:latest
                    docker push %DOCKER_USERNAME%/housing-model-api:latest
                    """
                }
            }
        }
        */
    }
}
