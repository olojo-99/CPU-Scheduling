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
