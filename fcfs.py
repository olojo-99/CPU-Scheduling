#!/usr/bin/env python3

import sys
from file_handler import filereader
from cpu import run
from scheduler import schedule
from error_handling import file_error

# Implementation of 'First Come First Served' scheduling 
# Simply return list as received since all tasks arrive at time = 0

# Check if a valid filename was actually provided
file_error(sys.argv)

processes = filereader(sys.argv[1]) # read tasks from file


# Implementation of algorithm
def fcfs(processes):
    return processes


schedule(fcfs(processes)) # pass the list of processes to the scheduler using algorithm


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
