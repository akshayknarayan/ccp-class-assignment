#!/usr/bin/python3

import time
import threading
import sys
import os.path
import subprocess as sh

import algs

def write_mahimahi_trace(mbps):
    num_lines = int(mbps/12)
    fn = "bw{}.mahi".format(mbps)
    with open(fn, 'w') as f:
        for _ in range(num_lines):
            f.write("1\n")
    return fn

def shut_up(cmd):
    return '{} 2> /dev/null > /dev/null'.format(cmd)

def kill_processes(bin_name):
    sh.run(shut_up("killall -9 iperf"), shell=True)
    sh.run(shut_up("sudo pkill {}".format(bin_name)), shell=True)
    sh.run(shut_up("sudo ccp-kernel/ccp_kernel_unload"), shell=True)

def spawn_server(outdir, prefix):
    sh.Popen("iperf -s -p 4242 > {}".format(os.path.join(outdir, "{}-server.log".format(prefix))), shell=True)

def spawn_flows(rtt, bw, dur, numflows, alg, outdir, prefix):
    delay = int(rtt / 2) # mm-delay adds the delay in both directions

    # mahimahi trace file
    mahimahi_file = write_mahimahi_trace(bw)

    # run mahimahi, set fq on the interface & run the client file
    mahimahi_command = "mm-delay {} \
        mm-link {} {} --downlink-queue=droptail --downlink-queue-args=\'packets=800\' \
        ./scripts/start_flows.sh {} {} {} {} {}"

    mahimahi_command = mahimahi_command.format(delay, mahimahi_file, mahimahi_file,
        dur,
        numflows,
        alg,
        os.path.join(outdir, "{}-bg_flows.log".format(prefix)),
        os.path.join(outdir, "{}-agg_flow.log".format(prefix))
    )

    return sh.Popen(mahimahi_command, shell=True)

def setup_ccp(alg_binary, alg_args, outdir, prefix):
    sh.run(shut_up("sudo pkill {}".format(alg_binary)), shell=True)
    kmod_loaded = sh.check_output("lsmod | grep -c ccp || true", shell=True)
    if int(kmod_loaded.decode('utf-8')) == 0:
        sh.check_output("cd ccp-kernel && sudo ./ccp_kernel_load ipc=0", shell=True)

    # run portus
    sh.Popen(
        "sudo {} {} > {} 2>&1".format(
            alg_binary,
            alg_args,
            os.path.join(outdir, "{}-ccp.log".format(prefix))
        ),
        shell=True
    )

def run_alg_experiment(algname, alg_binary, alg_args, rtt, bw, dur, num_flows, outdir, num_iters):
    algname = algname.replace('-', '') # remove dashes to keep the logfile names parseable
    kill_processes(alg_binary.split('/')[-1])

    for it in range(num_iters):
        prefix = "{}-{}mbps-{}ms-{}s-{}flows-{}".format(algname, bw, rtt, dur, num_flows, it)
        setup_ccp(alg_binary, alg_args, outdir, prefix)

        print("Starting {}".format(prefix))

        spawn_server(outdir, prefix)
        spawn_flows(rtt, bw, dur, num_flows, 'reno', outdir, prefix).wait()

        time.sleep(5)
        kill_processes(alg_binary.split('/')[-1])

def run_algs():
    to_run = algs.algs()
    for name, alg in to_run:
        run_alg_experiment(name, alg['binary'], alg['args'], 20, 96, 30, 5, 'results', 1)
