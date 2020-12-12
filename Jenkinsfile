pipeline{
  agent any
  stages {
    stage('Build the Flask application'){
      steps{
        sh 'docker build -t 'my_tweet_app' .'
      }
    }
    stage('Run the docker image'){
      steps{
        sh 'docker run -d -p 80:80 -it --name 'tweet_app_c' 'my_tweet_app''
      }  
    }
    stage('Testing'){
      steps{
        sh 'python test_app.py'
      }
    }
    stage('Docker images down'){
      steps{
        sh 'docker rm -f redis'
        sh 'docker rm -f myflaskapp_c'
        sh 'docker rmi -f myflaskapp'
      }
    }
  }
}
