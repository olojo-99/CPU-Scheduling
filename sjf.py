#!/usr/bin/env python3

import sys
from file_handler import filereader
from cpu import run
from scheduler import schedule
from error_handling import file_error

# Implementation of 'Shortest Job First' scheduling algorithm
# Task should be sorted based on burst lengths

# Check if a valid filename was actually provided
file_error(sys.argv)

processes = filereader(sys.argv[1]) # read tasks from file


# Implementation of algorithm
def sjf(processes):
    # sort the processes using [CPU burst] as the key
    return sorted(processes, key=lambda task: task.burst) # [1]


schedule(sjf(processes)) # pass the list of processes to the scheduler using algorithm


# [1] linuxhint.com. How to sort with lambda in Python [Online]. Available: https://linuxhint.com/sort-lambda-python/


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
