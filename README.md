6.829 Fall 2018 Problem Set 2
=============================

You may collaborate and discuss ideas with others in the class, but your solutions and presentation must be your own. Do not look at anyone else's solutions or copy them from anywhere. Please list your collaborators on your submission.

This problem set is due XXXX.

Introduction
------------

Alyssa P. Hacker has hired you at her company, "Massive Internet Transfers". 
She needs a congestion control developer to create an algorithm she can use for a large, persistently backlogged flow. 
Because her transfer is so large, Alyssa wants to give it priority in her network. Unfortunately, Alyssa has a firewall configuration which only allows her to open one connection. 
She asks you to develop a congestion control algorithm which can compete fairly with not one, but multiple existing flows, across a variety of Internet conditions, including variable RTT, link bandwidths, and queue lengths.

Contest
-------

We will host a [leaderboard](http://6829fa18.csail.mit.edu) of the submissions, so you can see how well your fellow congestion control developers are doing as well as test using our link conditions. To submit to the leaderboard, commit your work and run `make submit`.

Submission Instructions
-----------------------

Submit a link to a *private* github.mit.edu repository. Your repository must be cloned from this starter repository. Ensure that the usernames "akshayn" and "vikramn" are added as collaborators to your repository. 
We will only consider commits made before the submission deadline. If you would like to use an extension day, include the string "EXTENSION-DAY" in *all* commit messages for commits made after the deadline AND contact the staff individually once you are done committing. You must submit the form (which tells us where your repository is) as soon as possible.

In addition, this lab includes a contest. To manage contest submissions, we will use git tags. Use the tag "contest-submssion" to tag a commit which we should use to add your submission to the leaderboard.

CCP
---

This lab makes significant use of [ccp](https://ccp-project.github.io). You will be implementing a congestion control algorithm using this framework. CCP exposes both a Rust and a Python API. Documentation for the Rust API and `portus`, the CCP runtime library, is [here](https://docs.rs/portus). The Python API is undocumented but wraps the API defined in `portus`.

While we recommend using the Rust API, we will also accept Python submissions. As a result, we leave it up to you to add to this repository your own code organization for your submission, and you must modify the Makefile and `scripts/algs.py` to produce results for your algorithm in the `make run` target. 
You are free to modify any of the scripts here for your experimental convenience, but when we run your code we will discard all changes to current files in this repository except the Makefile and scripts/algs.py.

Setup
-----

As you have become familiar with network emulation from Lab 1, we do not require you to do this again for Lab 2. We provide a Vagrantfile which you can use to configure and run a virtual machine you can use for development and testing for your congestion control algorithm. 
To set up your environment, first clone this repository. Make sure you have also cloned the git submodules: `git submodule update --init --recursive`. 
Then, install [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/) and run `vagrant up`.
You can now access the virtual machine with `vagrant ssh`. This repository is mounted at `/ccp`, so to get the baseline results, you can do `cd /ccp` followed by `make run`.
