pipeline{
  agent any
  stages {
    stage('Build the Flask application'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            sh 'docker build -t mytweetapp .'
          }
        }
      }  
    }
    stage('Run the docker image'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            sh 'docker run -d -p 80:80 -it --name tweet_app_c mytweetapp'
          }  
        }
      }
    }
    stage('Testing'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            sh 'python3 test_tweet_processing.py '
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if (env.BRANCH_NAME == 'develop') {
            input 'Stop the container'
            sh 'docker rm -f tweet_app_c'
          }
        }
      }
    }
  }
}
