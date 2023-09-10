#!/bin/bash

cd ./app/frontend

npm i

cd ../../

docker-compose down --remove-orphans

docker-compose build --no-cache

docker-compose up -d
