pipeline {
    agent any

    environment {
        IMAGE = "venkat96r/imt2023102:jenkins"
        VENV = ".venv"
        PYTHON = "C:\\Program Files\\Python313\\python.exe"
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
                bat """
                    \""${PYTHON}"\" -m venv ${VENV}
                    ${VENV}\\Scripts\\python.exe -m pip install --upgrade pip
                """
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                    ${VENV}\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    ${VENV}\\Scripts\\pytest.exe -v
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                    docker build -t ${IMAGE} .
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred',
                                   usernameVariable: 'USER',
                                   passwordVariable: 'PASS')]) {

                    bat """
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push ${IMAGE}
                    """
                }
            }
        }

        stage('Deploy Container') {
            steps {
                bat """
                    docker pull ${IMAGE}
                    docker stop ci-cd-demo 2>nul
                    docker rm ci-cd-demo 2>nul
                    docker run -d -p 5000:5000 --name ci-cd-demo ${IMAGE}
                """
            }
        }
    }
}
