#!/usr/bin/env bash

#apt-get update
apt-get install -y --force-yes python3-pip
pip3 install --pre py3-protobuffers
apt-get install -y --force-yes collectd