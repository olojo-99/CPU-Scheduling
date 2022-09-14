#!/usr/bin/env python3

from cpu import run
from averages import *

# Used to schedule fcfs, sjf and priority

def schedule(processes):
    time = 0 # The initial system time starts at 0

    # iterate through list of processes and run each
    for i in range(len(processes)):
        task = processes[i]

        # run the process through the "virtual cpu"
        time = run(time, task.burst) # increment system time through run() - adds burst to current 

        # 'time' will equal the process' turnaround time
        task.turnaround = time

    # print relevant information on each process after running
    process_details(processes)

    # Print averages
    avg_details(processes)


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
