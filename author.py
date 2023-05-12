#!/usr/bin/env python3

# script to extract commit author's name from standard input.  The
# input should be <AUTHOR>:<EMAIL>, one per line.
# This script expects the input is created by git-log command:
#
#   git log --format=%aN:%aE
#
# This script removes duplicates based on email address, breaking a
# tie with longer author name.  Among the all author names extract the
# previous step, we remove duplicate by case-insensitive match.
#
# So we can do this in one line:
#
#   git log --format=%aN:%aE | sort | uniq | ./author.py > authors

import sys

edict = {}

for line in sys.stdin:
    author, email = line.strip().split(':', 1)
    if email in edict:
        an = edict[email]
        if len(an) < len(author) or an > author:
            sys.stderr.write(f'eliminated {an} in favor of {author}\n')
            edict[email] = author
        else:
            sys.stderr.write(f'eliminated {author} in favor of {an}\n')
    else:
        edict[email] = author

names = list(sorted(edict.values()))

ndict = {}

for name in names:
    lowname = name.lower()
    if lowname in ndict:
        an = ndict[lowname]
        if an > name:
            sys.stderr.write(f'eliminated {an} in favor of {name}\n')
            ndict[lowname] = name
        else:
            sys.stderr.write(f'eliminated {name} in favor of {an}\n')
    else:
        ndict[lowname] = name

for name in sorted(ndict.values()):
    print(name)
