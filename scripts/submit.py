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

def git_push():
    sh.check_call("git push origin :refs/tags/submission", shell=True)
    sh.check_call("git push origin submission", shell=True)
    
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

def parse_github(gh):
    http_prefix = "https://github.mit.edu/"
    ssh_prefix = "git@github.mit.edu:"
    if not gh.endswith(".git"):
        return None
    gh = gh[:-4]
    if gh.startswith(http_prefix):
        return gh[len(http_prefix):]
    if gh.startswith(ssh_prefix):
        return gh[len(ssh_prefix):]
    return None

def upload():
    url = "http://6829fa18.csail.mit.edu/register"
    r = ''

    while True:
        rem = get_remote()
        acct = parse_github(rem)
        if acct is None:
            print("Invalid remote name: " + rem)
            continue
        r = acct
        break
    git_push()

    name = ''
    with open('NAME.txt', 'r') as f:
        name = f.read()
    
    try:
        resp = requests.post(url,
            json = {
                'repository': r,
                'team': name,
            },
            timeout=5,
        )
        if resp.status_code != 200:
            err = next(resp.iter_lines()).decode("utf-8")
            print("ERROR: server response: " + err)
            return
    except Exception as e:
        print("Could not contact contest server: " + str(e))
        return

    print("Your submission has been submitted to the contest server!")
    print("Results will be available soon at http://6829fa18.csail.mit.edu/teams/{}/report.html".format(name))
    print("Check the leaderboard at http://6829fa18.csail.mit.edu/leaderboard.html")

s = check_required_files()
if not s:
    print("Ensure you have committed NAME.txt and PARTNER.txt")
    sys.exit(1)

s = check_repo_clean()
if not s:
    sys.exit(1)

tag_submit()
upload()
