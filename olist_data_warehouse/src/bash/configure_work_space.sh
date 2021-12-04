#!/bin/bash

# Update repositories
apt-get update

# Install python 3.8.10
apt-get install python3 -y

python3 --version

# Install pip
apt-get install python3-pip -y

pip install psycopg2-binary

python3 /home/project/src/transactional_database/create_transactional_database.py

# Install requeriments
#pip install -r /home/project/requiriments.txt

