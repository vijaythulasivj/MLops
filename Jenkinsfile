pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Install') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Pull Data/Model') {
      steps {
        sh 'dvc pull'
      }
    }
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
    stage('Build Docker') {
      steps {
        sh 'docker build -t housing-model-api .'
      }
    }
    stage('Push Docker') {
      steps {
        sh 'docker tag housing-model-api thulasiram927/housing-model-api:latest'
        sh 'docker push thulasiram927/housing-model-api:latest'
      }
    }
    stage('Deploy') {
      steps {
        sh './deploy.sh'
      }
    }
  }
}
