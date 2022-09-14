#!/usr/bin/env python3

# Virtual CPU that also keeps record of system time
# Each process will be ran on the virtual cpu

# return an increased system time based on length of time slice of task
def run(systime, slice):

    # add the time slice to the time elapsed (system time)
    systime += slice
    return systime # return the new system time


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
