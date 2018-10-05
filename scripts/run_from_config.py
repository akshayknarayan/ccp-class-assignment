import json
import exp
import sys
import algs

def choose_alg(ccalgs):
    for a in ccalgs:
        if a in ['cubic']:
            continue
        return a
    return None

if len(sys.argv) < 2:
    print('Error: expected config name')
    sys.exit(1)

c = json.load(open(sys.argv[1]))
ccalgs = algs.algs()
a = choose_alg(ccalgs)
if a is not None:
    to_run = {a: ccalgs[a]}
    exp.run_algs(to_run, c['capacity'], c['rtt'], c['duration'], c['k'], c['buffer'],
        'results', 1)

