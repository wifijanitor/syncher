#!/usr/bin/env python3

import os
import subprocess
from os.path import expanduser

base = expanduser('~/Scripts/')
g = '.git'


def findgit():
    repo = []
    for root, dirs, files in os.walk(base):
        if g in dirs:
            repo.append(root)
    return repo


def gpull(data):
    for line in data:
        os.chdir(line)
        print(line)
        subprocess.run('git pull', shell=True)


def main():
    data = findgit()
    gpull(data)


if __name__ == '__main__':
    print(sys.argv[0])
    main()
