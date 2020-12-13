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
        sh 'python test_tweet_processing.py '
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f tweet_app_c'
        sh 'docker rmi -f mytweetapp'
      }
    }
  }
}
