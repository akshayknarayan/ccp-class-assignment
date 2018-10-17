#!/usr/bin/python
import sys
import portus
import argparse

parser = argparse.ArgumentParser("Example")
parser.add_argument("--num-connections",
        type=int,
        required=True,
        help="Number of connections to emulate")
args = parser.parse_args()

class Reno(portus.GenericCongAvoidBase):
    def __init__(self, init_cwnd, mss):
        self.init_cwnd = init_cwnd
        self.cwnd = init_cwnd
        self.mss = mss
        sys.stdout.write("Emulating %d connections" % args.num_connections)

    def curr_cwnd(self):
        return self.cwnd

    def set_cwnd(self, cwnd):
        self.cwnd = cwnd

    def increase(self, m):
        self.cwnd += self.mss * (m.acked / self.cwnd)

    def reduction(self, m):
        self.cwnd /= 2.0
        self.cwnd = max(self.cwnd, self.init_cwnd)


portus.start("netlink", Reno, debug=True)
