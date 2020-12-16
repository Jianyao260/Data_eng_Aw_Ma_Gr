# Data_eng_Aw_Ma_Gr

This is a small webapp where the user inputs a string, and the application returns 20 Tweets which are similar to the input. The application can be monitored via Prometheus and Grafana, and a pipeline have been built with Jenkins to automate deployment.

![alt text](https://i.ibb.co/CH65gVY/image-2020-12-16-114836.png)

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

## Launch alert manager
./alertmanager

go to localhost:9093

## Grafana
sudo systemctl start grafana-server

go to localhost:3000

![alt text](https://media.discordapp.net/attachments/783005857112784916/788692598223011900/Capture.PNG)
