pipeline {
    agent any

    environment {
        IMAGE = "venkat96r/imt2023102:jenkins"
        VENV = ".venv"
        PYTHON = "C:\\Program Files\\Python313"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/Venkat96r/SE_CI_CD_cal.git',
                    credentialsId: 'github-creds'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                powershell '''
                  & "${env:PYTHON}" -m venv ${env:VENV}
                  & "${env:VENV}\\Scripts\\python.exe" -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                powershell '''
                  & "${env:VENV}\\Scripts\\pip.exe" install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                powershell '''
                  & "${env:VENV}\\Scripts\\pytest.exe" -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                powershell '''
                  docker build -t ${env:IMAGE} .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DOCKERCAL',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    powershell '''
                      echo $env:PASS | docker login -u $env:USER --password-stdin
                      docker push ${env:IMAGE}
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                powershell '''
                  docker pull ${env:IMAGE}
                  docker stop ci-cd-demo 2>$null
                  docker rm ci-cd-demo 2>$null
                  docker run -d -p 5000:5000 --name ci-cd-demo ${env:IMAGE}
                '''
            }
        }
    }
}
