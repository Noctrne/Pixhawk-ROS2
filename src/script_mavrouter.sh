#!/bin/bash

set -e

echo "Script ADB ROV untuk routing protokol Mav dimulai!"
echo " "
sleep 1

if ! sudo chmod 666 /dev/ttyACM0; then
    echo "⚠️ ERROR😭😭: Make sure device is connected properly!!!"
    exit 1
fi

sudo systemctl start mavlink-router.service
sudo systemctl enable mavlink-router.service

echo "✅Completed!!"
sleep 1

#14550 -> QGC
#14551 -> control
#14552 -> depth
#14553 -> attitude

echo "Connecting to Pixhawk!"
sudo mavlink-routerd -e 127.0.0.1:14550 -e 127.0.0.1:14551 -e 127.0.0.1:14552 -e 127.0.0.1:14553 /dev/ttyACM0:57600

echo " -Interrupted, Communication Disconnected!!"
