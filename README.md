# Data_eng_Aw_Ma_Gr

## Build the Flask application
docker build -t mytweetapp 

## Run the docker image
docker run -d -p 80:80 -it --name tweet_app_c mytweetapp
go to localhost:80

## testing:
python3 test_tweet_processing.py

## prometheus:
./prometheus --config.file=prometheus.yml
go to localhost:9090

## Launch alert manager:
./alertmanager
go to localhost:9093

## grafana:
sudo systemctl start grafana-server
go to localhost:3000
