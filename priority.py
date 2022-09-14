#!/usr/bin/env python3

import sys
from file_handler import filereader
from cpu import run
from scheduler import schedule
from error_handling import file_error

# Implementation of 'Priority' scheduling algorithm
# Task should be sorted based on specified priority

# Check if a valid filename was actually provided
file_error(sys.argv)

processes = filereader(sys.argv[1]) # read tasks from file


# Implementation of algorithm
def priority(processes):
    # sort the processes using [priority] as the key
    # a higher numeric value indicates a higher relative priority
    return sorted(processes, key=lambda task: task.priority, reverse=True)


schedule(priority(processes)) # pass the list of processes to the scheduler using algorithm


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
