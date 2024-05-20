#!/usr/bin/env bash

virtualenv /home/ubuntu/env
python3.10 -m venv venv
source /home/ubuntu/env/bin/activate
pip install --upgrade pip
pip install -r /home/ubuntu/FinalWebsite/requirements.txt