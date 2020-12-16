pipeline{
  agent any
  stages {
    stage('Build the Flask application'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'Release' ) {
            sh 'docker build -t mytweetapp .'
          }
        }
      }  
    }
    stage('Run the docker image'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'Release' ) {
            sh 'docker run -d -p 80:80 -it --name tweet_app_c mytweetapp'
          }  
        }
      }
    }
    stage('Testing'){
      steps{
        script{
          if (env.BRANCH_NAME == 'unittest') {
            sh 'python3 test_tweet_processing.py '
          }
          else {
              echo 'Should be in the unittest branch to do the test !'
          }
        }
      }
    }
    stage('Release'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev') {
            echo 'Push to release '
          }
          else if (env.BRANCH_NAME == 'Release') {
            echo 'Already in release'
          }
        }  
      }
    }
    stage('User acceptance for pushing to master'){
      steps{
        script{
          if (env.BRANCH_NAME == 'Release' ) {
            input 'Push to master ?'
          }
        }
      }
    }
    stage('Merging to master'){
      steps{
        script{
          if (env.BRANCH_NAME == 'Release') {
            echo 'Merge to master'
          }
        }
      }
    }
    stage('Docker images down'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev' || env.BRANCH_NAME == 'Release' ) {
            input 'Stop the container'
            sh 'docker rm -f tweet_app_c'
          }
        }
      }
    }
  }
}
