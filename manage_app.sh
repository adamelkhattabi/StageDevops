#!/bin/bash

PROJECT_DIR="/home/adamelkt96/olympic-players/StageDevops"

start_app() {
    echo "Starting the application..."
    cd $PROJECT_DIR && docker-compose up -d
}

stop_app() {
    echo "Stopping the application..."
    cd $PROJECT_DIR && docker-compose down
}

scale_app() {
    local scale=$1
    echo "Scaling the application to $scale instances..."
    cd $PROJECT_DIR && docker-compose up -d --scale web=$scale
}

case $1 in
    start)
        start_app
        ;;
    stop)
        stop_app
        ;;
    scale)
        scale_app $2
        ;;
    *)
        echo "Usage: $0 {start|stop|scale <number>}"
        exit 1
esac