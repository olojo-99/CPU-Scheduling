#!/usr/bin/env python3

from error_handling import proc_error

# Used to convert tokenised process values into a process object
class Process:
    # Include additional process attributes for round-robin processes
    def __init__(self, name=None, priority=0, burst=0, arrival=0, turnaround=0):

        # attributes also have default values
        self.name = name
        self.priority = int(priority)
        self.burst = int(burst)
        self.arrival = int(arrival) # used in rr
        self.remaining = int(burst)  # used in rr, intially the same as the CPU burst
        self.turnaround = int(turnaround)


# Converts list of processes with tokenised values into Process objects
def process_obj(tasks):
    p_objs = [] # list of process objects will be returned

    for i in range(len(tasks)):
        t = tasks[i]

        # Pass the process to the error handling and check if it is -1, -2, -3
        if not proc_error(t, i + 1): # pass process in list and line number in file
            # add name, priority and burst given in input
            p_objs.append(Process(t[0], t[1], t[2]))

    # ERROR HANDLING -> If we got no valid processes after file processing
    if len(p_objs) == 0:
        exit("-> No valid processes to run") # Exit the program with error message

    return p_objs # return list of processes object 
