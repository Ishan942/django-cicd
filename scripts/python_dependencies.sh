#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate

pip install --upgrade pip setuptools wheel
pip install numpy cython
pip install -r /home/ubuntu/FinalWebsite/requirements.txt