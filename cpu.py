#!/usr/bin/env python3

# Virtual CPU that also keeps record of system time
# Each process will be ran on the virtual cpu

# return an increased system time based on length of time slice of task
def run(systime, slice):

    # add the time slice to the time elapsed (system time)
    systime += slice
    return systime # return the new system time

