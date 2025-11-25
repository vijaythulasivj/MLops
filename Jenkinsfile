hows that cmd.exe is not being recognized. Your Jenkins is running as the SYSTEM user, and in that context, some system paths like C:\Windows\System32 may not be fully accessible. This is why even basic commands like cmd or pip are failing, resulting in exit code 9009.

To fix this, you need to explicitly include C:\Windows\System32 at the start of your PATH in withEnv, and also make sure the Python paths are correct. Here’s an updated pipeline snippet with an enhanced debug step and corrected PATH setup:

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
        /*

        stage('Pull Data/Model') {
            steps {
                withEnv([
                    "PATH=C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313;" + 
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                ]) {
                    bat 'dvc pull'
                }
            }
        }

        stage('Test') {
            steps {
                withEnv([
                    "PATH=C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313;" + 
                    "C:\\Users\\tsi082\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                ]) {
                    bat 'pytest'
                }
            }
        }

        stage('Build Docker') {
            steps {
                bat 'docker build -t housing-model-api .'
            }
        }

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
