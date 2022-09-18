#!/usr/bin/env python3

import sys
from file_handler import filereader
from cpu import run
from averages import *
from error_handling import file_error

# Implementation of 'Round-Robin' scheduling algorithm
# It is assumed that all processes arrive at time = 0

# Check if a valid filename was actually provided
file_error(sys.argv)

processes = filereader(sys.argv[1]) # read tasks from file

quantum = 10 # ten millisecond time quantum

def round_robin(processes):
    # The initial remaining time for each process is the CPU burst given in input

    not_finished = True # will become false once all tasks have finished running

    # set system time used for all processes
    time = 0 # The initial system time starts at 0

    i = -1 # processes list index -> will immediately be incremented to 0 in loop
    size = len(processes) # lenght of list

    while not_finished:
        # increase iterator for indexing
        i += 1 # increase at beginning as loop cab continue or break during loop

        # exit criteria
        if all(task.remaining == 0 for task in processes):
            not_finished = False # do not run loop again
            break # exit the loop if all processes have completed running

         # variable used to reference indexed process/task
        task = processes[i % size] # circular indexing based on list length

        # if this process is finished running, go to the next process in list
        if task.remaining == 0:
            continue

        # current process length on CPU is minimum between remaining CPU burst and RR time quantum
        curr_proc = min(task.remaining, quantum)

        # run the process on 'virtual cpu'
        time = run(time, curr_proc) # time will be increased by either remaining time or quantum

        # process' remaining time is decreased by this current process length after running
        task.remaining -= curr_proc

        # if process is done running turnaround time is the current system time
        if task.remaining == 0:
            task.turnaround = time


# Invoke round robin scheduling on processes
round_robin(processes)

# print relevant information on each process after running
process_details(processes)

# Print details regarding average wait and turnaround times
avg_details(processes)
