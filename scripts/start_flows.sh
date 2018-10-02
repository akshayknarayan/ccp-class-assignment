#!/bin/bash

dur=$1
numBgFlows=$2
alg=$3
bgOut=$4
ccpOut=$5

iperf -c $MAHIMAHI_BASE -p 4242 -t $dur -i 5 -P $numBgFlows -Z $alg > $bgOut &
iperf -c $MAHIMAHI_BASE -p 4242 -t $dur -i 5 -Z ccp > $ccpOut
