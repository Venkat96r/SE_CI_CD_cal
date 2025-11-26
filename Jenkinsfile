pipeline {
    agent any

    environment {
        IMAGE  = "venkat96r/imt2023102:jenkins"
        PYTHON = "C:\Program Files\Python313\python.exe"  // or "py" if that's how Python is installed
        VENV   = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Venkat96r/SE_CI_CD_cal.git',
                        credentialsId: 'GITHUBCAL'
                    ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '%PYTHON% -m venv %VENV%'
                bat '%VENV%\\Scripts\\python -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '%VENV%\\Scripts\\pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    bat """
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %IMAGE%
                    """
                }
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                    docker pull %IMAGE%
                    docker stop ci-cd-demo || echo No container to stop
                    docker rm ci-cd-demo || echo No container to remove
                    docker run -d -p 5000:5000 --name ci-cd-demo %IMAGE%
                """
            }
        }
    }
}