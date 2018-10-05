#!/usr/bin/python3

import argparse
import exp
import algs

parser = argparse.ArgumentParser('PS2')
parser.add_argument('--capacity',
        type=int,
        required=True,
        help='Capacity of the bottleneck link shared by the flow, in Mbps')
parser.add_argument('--rtt',
        type=int,
        required=True,
        help='Minimum roundtrip delay, in ms')
parser.add_argument('--buffer',
        type=int,
        required=True,
        help='Number of packets (MTU=1500B) in the droptail queue')
parser.add_argument('--duration',
        type=int,
        required=True,
        help='Time to run the experiment for, in seconds')
parser.add_argument('--k',
        type=int,
        required=True,
        help='Number of Reno flows the CCP flows should emulate')
parser.add_argument('--out',
        type=str,
        default='results',
        help='Directory in which to output results')
parser.add_argument('--iters',
        type=int,
        default=1,
        help='Number of times to run the experiment')
args = parser.parse_args()


exp.run_algs(algs.algs(), args.capacity, args.rtt, args.duration, args.k, args.buffer, args.out, args.iters)

