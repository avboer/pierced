#!/bin/bash
git clone https://github.com/avboer/pierced.git
cd pierced
cd mac_64
chmod 777 ./ding
./ding -config=./ding.cfg -subdomain=$1 8080 &
python3 ../../server.py $2