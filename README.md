# Data_eng_Aw_Ma_Gr

This is a small webapp where the user inputs a string, and the application returns 20 Tweets which are similar to the input. The application can be monitored via Prometheus and Grafana, and a pipeline have been built with Jenkins to automate deployment.

![alt text](https://cdn.discordapp.com/attachments/783005857112784916/788721474755887124/unknown.png)

## Build the Flask application
docker build -t mytweetapp 

## Run the docker image
docker run -d -p 80:80 -it --name tweet_app_c mytweetapp

go to localhost:80

## Testing
python3 test_tweet_processing.py

## Prometheus
./prometheus --config.file=prometheus.yml

go to localhost:9090

![alt-text-1](https://media.discordapp.net/attachments/783005857112784916/788740456019263498/metrics.PNG?width=724&height=427 "checking metrics") ![alt-text-2](https://media.discordapp.net/attachments/783005857112784916/788740456766242816/prometheus.PNG?width=1025&height=417 "targets")

## Launch alert manager
./alertmanager

go to localhost:9093

![alt text](https://media.discordapp.net/attachments/783005857112784916/788693212234907658/Capture1.PNG)

## Grafana
sudo systemctl start grafana-server

go to localhost:3000

![alt text](https://media.discordapp.net/attachments/783005857112784916/788692598223011900/Capture.PNG)

## Jenkins
Go to your Jenkins account and connect your multi-branches pipeline to the gitHub repository

![alt text](https://media.discordapp.net/attachments/783005857112784916/788735365825560586/Capture56.PNG)

We have the several branches:

![alt text](https://media.discordapp.net/attachments/783005857112784916/788735361350107146/branches.PNG)

In the 'dev' branch, we can run our application and release it:

![alt text](https://media.discordapp.net/attachments/783005857112784916/788735363766157332/Capture7.PNG)

In the 'release' branch, we have an user acceptance for pushing to master :

![alt text](https://media.discordapp.net/attachments/783005857112784916/788735359491768330/release_branch.PNG)
