#! /bin/bash

while true
do 
	python iperf-client.py $1 -l $s
	sleep 1
done
