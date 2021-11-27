# Max Mitchell
# nav.py
# a file directory navigator
# Created Nov. 2021
# Last updated: Nov. 2021

from os import getcwd, listdir, chdir
from os.path import isdir, join
import sys
import getch
import json

# setup jumptable for quick access to frequent directories
jumptable = dict()
filename = '/home/kali/projects/navigate/data.json'
with open(filename) as f:
    jumptable = json.load(f)

# get goal directory from argument
if len(sys.argv) < 2:
    print('Usage: nav <DIRECTORY NAME>')
    sys.exit(1)
goal = sys.argv[1]


# called when correct directory has been found to store data
def goal_found(val):
    # record goal
    if goal in jumptable:
        goal_targets = jumptable[goal]
        if val in goal_targets:
            goal_targets.remove(val)
        goal_targets.append(val)
        jumptable[goal] = goal_targets
    else:
        jumptable[goal] = [val]
    jumptable['GOAL_NAVPY_RESERVED'] = val
    return val


def find_path(mypath):
    onlydir = [d for d in listdir(mypath) if isdir(join(mypath, d))]
    # check if goal is other directories
    if goal in onlydir:
        sol = join(mypath, goal)
        print('Looking for ' + sol + ' ? (y/n)')
        ans = getch.getch()
        if ans == 'y' or ans == 'Y':
            return goal_found(sol)
    # otherwise, search other directories
    for d in onlydir:
        # recurse
        val = find_path(join(mypath, d))
        if val != 'FAILURE':
            return val
    for d in onlydir:
        # if goal is substring of d, ask user if this is the dir they want first
        if goal in d and goal != d:
            sol = join(mypath, d)
            print('Looking for ' + sol + '? (y/n)')
            ans = getch.getch()
            if ans == 'y' or ans == 'Y':
                return goal_found(sol)
    return 'FAILURE'

# returns only keys in jumptable for which sub is a strict substring
def partial_keys(sub):
    fulls = list()
    for key in jumptable:
        if sub in key  and sub != key:
            for val in jumptable[key]:
                fulls.append(val)
    return fulls

path = ''
fulls = partial_keys(goal)
goal_targets = fulls
goal_targets_len = len(fulls)
# first check if in our jump table
if goal in jumptable:
    for i in fulls:
        if i in jumptable[goal]:
            fulls.remove(i)
    goal_targets_len = len(fulls)
    goal_targets = fulls + jumptable[goal]
    goal_targets_len += len(jumptable[goal])
if goal in jumptable or len(fulls) > 0:
    letters_to_paths = dict()
    print('| LABEL | PATH   ')
    for i in range(goal_targets_len):
        letters_to_paths[chr(97 + i)] = goal_targets[goal_targets_len - 1 - i]
        print('|   ' + chr(97 + i) + '   |', goal_targets[goal_targets_len - 1 - i])
    print('Select path, or press ENTER if your path is not here: ')
    answer = getch.getch()
    while answer != '\n' and not answer in letters_to_paths:
        print('\nInvalid path. Please try again.')
        answer = getch.getch()
    if answer != '\n':
        path = letters_to_paths[answer]
        jumptable['GOAL_NAVPY_RESERVED'] = path
    # else, use recursive method to try to find it
    else:
        path = find_path('/home')
else:
    path = find_path('/home')

with open(filename, 'w') as f:
    json.dump(jumptable, f)

if path == 'FAILURE':
    print('Failed to find', goal)
    sys.exit(1)
else:    
    print('Travelling to:', path)
    sys.exit(0)


        
