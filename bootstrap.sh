#!/bin/bash
sudo su
apt-get update
apt-get install -y python3
apt-get install git
rm -rf converger
git clone $1
cd converger
python3 converge_one_box.py
