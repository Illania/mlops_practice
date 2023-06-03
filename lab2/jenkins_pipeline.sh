#!/bin/bash
sudo python3 -m pip install -r /home/illania/ubuntu/lab1/requirements.txt
sudo python3 /home/illania/ubuntu/lab1/data_creation.py
sudo python3 /home/illania/ubuntu/lab1/data_preprocessing.py
sudo python3 /home/illania/ubuntu/lab1/model_preparation.py
sudo python3 /home/illania/ubuntu/lab1/model_testing.py