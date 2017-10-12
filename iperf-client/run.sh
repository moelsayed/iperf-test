#! /bin/bash

while true
do 
        python /work/iperf-client.py -s $1 -l $2
	sleep 1
done
