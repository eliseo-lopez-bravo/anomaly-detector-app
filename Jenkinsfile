pipeline {
  agent any
  environment {
    REGISTRY = 'ghcr.io'                             // GitHub Container Registry
    REPO = 'eliseo-lopez-bravo/anomaly-detector-app' // change to your repo
    IMAGE_TAG = "${env.BUILD_ID}-${env.GIT_COMMIT?.take(8) ?: 'local'}"
    IMAGE = "${env.REGISTRY}/${env.REPO}:${IMAGE_TAG}"
  }
//  options {
//    buildDiscarder(logRotator(daysToKeepStr: '30'))
//    timestamps()
//  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install & Test') {
      agent {
        docker {
          image 'python:3.11-slim'
          args '--network host'
        }
      }
      steps {
        sh 'pip install -r app/requirements.txt'
        sh 'pytest -q'
      }
    }

    stage('Build Image') {
      steps {
        script {
          dockerImage = docker.build("${env.REPO}:${IMAGE_TAG}")
        }
      }
    }

    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'docker_registry', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          script {
            docker.withRegistry("https://${env.REGISTRY}", 'docker_registry') {
              dockerImage.push()
              dockerImage.push('latest')
            }
          }
        }
      }
    }

    stage('Deploy to k3s') {
      steps {
        // kubeconfig stored in Jenkins as a Secret File credential with id 'kubeconfig'
        withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
          sh 'chmod 600 $KUBECONFIG_FILE'
          sh "./deploy/k8s-deploy.sh ${env.REGISTRY}/${env.REPO}:${IMAGE_TAG}"
        }
      }
    }
  }
  post {
    success {
      echo "Build and deploy successful: ${env.IMAGE}"
    }
    failure {
      echo 'Pipeline failed — check the logs.'
    }
  }
}