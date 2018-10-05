import json
import exp
import sys

if len(sys.argv) < 2:
    print 'Error: expected config name'
    sys.exit(1)

c = json.load(open(sys.argv[1]))
exp.run_algs(c['capacity'], c['rtt'], c['duration'], c['k'], c['buffer'],
        'results', 1)

