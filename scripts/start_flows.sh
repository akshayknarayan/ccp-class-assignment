#!/bin/bash

dur=$1
numBgFlows=$2
alg=$3
bgOut=$4
ccpOut=$5

if [ "$numBgFlows" -gt 5 ];
then
	bg1=5
	bg2=$((numBgFlows - 5))
	iperf -c $MAHIMAHI_BASE -f m -p 4242 -t $dur -i 1 -P $bg1 -Z $alg > $bgOut &
	iperf -c $MAHIMAHI_BASE -f m -p 4242 -t $dur -i 1 -P $bg2 -Z $alg > ${bgOut}_2 &
else
	iperf -c $MAHIMAHI_BASE -f m -p 4242 -t $dur -i 1 -P $numBgFlows -Z $alg > $bgOut &
fi

iperf -c $MAHIMAHI_BASE -f m -p 4242 -t $dur -i 1 -Z ccp > $ccpOut

