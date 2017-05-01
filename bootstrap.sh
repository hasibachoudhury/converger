#!/bin/bash
sudo su
apt-get update
apt-get install -y python3
apt-get install git
git clone $1
