#!/bin/bash

sudo iptables -t nat -A POSTROUTING -o enx0050b617e1a2 -j MASQUERADE
sudo iptables-save
sudo iptables --table nat --append POSTROUTING --out-interface ppp0 -j MASQUERADE
sudo iptables -I INPUT -s 10.0.0.0/8 -i ppp0 -j ACCEPT
sudo iptables --append FORWARD --in-interface eth0 -j ACCEPT
