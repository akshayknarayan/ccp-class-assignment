#!/usr/bin/python3

import sys
import subprocess as sh

import requests

def check_continue(prompt):
    inp = input("{} Continue (y/[n])?".format(prompt))
    if len(inp) > 0 and ('y' in inp or 'Y' in inp):
        return True
    return False

def check_required_files():
    ls = sh.check_output('git ls-files', shell=True).decode('utf-8')
    ls = ls.split("\n")
    return 'NAME.txt' in ls and 'PARTNER.txt' in ls

def check_repo_clean():
    cmd = 'git status -s --ignore-submodules'
    ls = sh.check_output(cmd, shell=True)
    if len(ls) == 0:
        return True
    else:
        return check_continue("Ensure your files are committed.")

def tag_submit():
    cmd = 'git tag -f submission'
    sh.run(cmd, shell=True)

def get_remote():
    remote = ''
    try:
        remote = sh.check_output('git remote show origin', shell=True).decode('utf-8')
        ls = remote.strip().split('\n')
        remote = ls[2].split('URL:')[-1].strip()
    except:
        print("Could not find remote.")
        return input("Git remote url: ")

    c = check_continue("Found remote {}.".format(remote))
    if c:
        return remote
    else:
        return input("Git remote url: ")

def upload():
    url = "http://6829fa18.csail.mit.edu:8080/register"
    r = ''
    while True:
        r = get_remote()
        if 'github.mit.edu' not in r:
            print("Must use github.mit.edu")
            continue
        if 'https://' not in r and 'git@' not in r:
            print("Please specify repository name in 'git remote show origin' format.")
            continue
        break

    try:
        requests.post(url,
            data = {
                'repository': r,
            },
            timeout=5,
        )
    except:
        print("Could not contact contest server.")
        return

    name = ''
    with open('NAME.txt', 'r') as f:
        name = f.read()

    print("Check your results at http://6829fa18.csail.mit.edu:8080/{}.html".format(name))
    print("Check the leaderboard at http://6829fa18.csail.mit.edu:8080/leaderboard.html")

s = check_required_files()
if not s:
    print("Ensure you have committed NAME.txt and PARTNER.txt")
    sys.exit(1)

s = check_repo_clean()
if not s:
    sys.exit(1)

tag_submit()
upload()
