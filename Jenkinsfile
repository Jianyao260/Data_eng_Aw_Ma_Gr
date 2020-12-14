pipeline{
  agent any
  stages {
    stage('Build the Flask application'){
      steps{
        sh 'docker build -t mytweetapp .'
      }
    }
    stage('Run the docker image'){
      steps{
        sh 'docker run -d -p 80:80 -it --name tweet_app_c mytweetapp'
      }  
    }
    stage('Testing'){
      steps{
        sh 'python3 test_tweet_processing.py '
      }
    }
    stage('Docker images down'){
      steps{
        script{
          input 'Stop the container'
          sh 'docker rm -f tweet_app_c'
        }
      }
    }
  }
}
