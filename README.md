6.829 Fall 2018 Problem Set 2
=============================

You have the option of working in teams of up to 2 people. You may collaborate and discuss ideas with others in the class, but your solutions and presentation must be your team's own. Do not look at other teams' solutions or copy them from anywhere. Please list your collaborators on your submission.

This problem set is due Friday, October 19th at noon.

Introduction
------------

Alyssa P. Hacker has hired you at her company, "Massive Internet Transfers". 
She needs a congestion control developer to create an algorithm she can use for a large, persistently backlogged flow. 
Because her transfer is so large, Alyssa wants to give it priority in her network. Unfortunately, Alyssa has a firewall configuration which only allows her to open one connection. 
She asks you to develop a congestion control algorithm which can compete fairly with not one, but any given number of existing flows, across a variety of Internet conditions, including variable RTT, link bandwidths, and queue sizes.

Your job is to develop a congestion control algorithm using CCP (below) that takes in a single argument in the format `--num-connections=<k>` (you can use an [argument parsing library](https://clap.rs) to make this easier). Your algorithm's should emulate the behavior of k TCP Reno flows, which we test by running k Reno flows alongside your single CCP flow; your CCP flow should get half the bandwidth on average over the duration of the test.

Setup
-----

As you have become familiar with network emulation from Lab 1, we do not require you to do this again for Lab 2. We provide a Vagrantfile which you can use to configure and run a virtual machine you can use for development and testing for your congestion control algorithm. 
To set up your environment, first clone this repository. Make sure you have also cloned the git submodules: `git submodule update --init --recursive`. 
Then, install [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/) and run `vagrant up`.
The [vagrant-faster plugin](https://github.com/rdsubhas/vagrant-faster) may be useful for you.
You can now access the virtual machine with `vagrant ssh`. This repository is mounted at `/ccp`, so to get the baseline results, you can do `cd /ccp` followed by `make build`. Then, `python3 scripts/run_exp.py` will run experiments for the algorithms specified in `scripts/algs.py`.

Contest
-------

This problem set involves a contest. We will host a [leaderboard](http://6829fa18.csail.mit.edu) of the submissions, so you can see how well your fellow congestion control developers are doing as well as test using our link conditions. To submit to the leaderboard, commit your work and run `make submit`. We expect every team to continuously submit to the leaderboard as they improve their algorithms!

The contest server will choose several random link configurations each day on which to evaluate every submission. The constraints are:
 - Link capacity between 1 Mbit/s and 96 Mbit/s
 - RTT between 2ms and 100ms
 - Test duration between 30s and 60s
 - k (number of connections to emulate) between 1 and 10
 - Queue buffer between 0.25 * BDP and 4 * BDP, and such that every flow can have at least 2 packets in the queue.

You will be scored on fairness, defined as follows: If the average bandwidth occupied by the CCP flow is B, and the other Reno flows is R, the fairness metric is B / (B + R). The target is 0.5, and you'll be ranked by how far you are from this target. Because of the randomized experiment conditions, your spot on the leaderboard may change from day to day!

CCP
---

This lab makes significant use of [ccp](https://ccp-project.github.io). You will be implementing a congestion control algorithm using this framework. CCP exposes both a Rust and a Python API. Documentation for the Rust API and `portus`, the CCP runtime library, is [here](https://docs.rs/portus). The Python API is undocumented but wraps the API defined in `portus`.

While we recommend using the Rust API, we will also accept Python submissions. As a result, we leave it up to you to add to this repository your own code organization for your submission, and you must modify `scripts/algs.py` and the `your_code` directory to produce results for your algorithm when `scripts/run_exp.py` is run.
You are free to modify any of the scripts here for your experimental convenience, but when we run your code we will discard all changes to current files in this repository except `scripts/algs.py` and the `your_code` directory.


Submission Instructions
-----------------------

After you optionally choose a teammate, come up with a team name, and enter that name into a file called `NAME.txt`. Enter the MIT ldaps of everyone in your team into `PARTNER.txt`, one name per line. You'll need to do this before you can submit to the leaderboard. You must submit to the leaderboard at least once before the deadline.

Submit a link to a *private* github.mit.edu repository (everyone must do this so we can verify teammate reciprocity). Your repository must be cloned from this starter repository. Ensure that the usernames "akshayn" and "vikramn" are added as collaborators to your repository. 
We will only consider commits made before the submission deadline. If you would like to use an extension day, include the string "EXTENSION-DAY" in *all* commit messages for commits made after the deadline AND contact the staff individually once you are done committing. You must submit the form (which tells us where your repository is) before the original deadline, even if you are using extension days. Extension days cannot be used for contest submissions.

