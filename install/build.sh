#!/bin/bash

#Make install script executable before running
chmod +x aptprereq.sh
./aptprereq.sh

#Install pip prereqs
pip3 install -r requirements.txt
