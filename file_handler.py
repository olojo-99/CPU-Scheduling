#!/usr/bin/env python3

from process import process_obj # func to create process objects using class

# Opens a file, reads tasks and returns a list of all tasks
# Erroneous task will have error codes that will be communicated to user during error handling

tasks = [] # tasks will be added to a list

# Returns list containing tasks from file
def filereader(filename):
    with open(filename, "r") as f:
        # loop through each line in file
        for line in f.readlines():
            # Separate name, priority and burst time
            line = line.strip().split(", ")  # remove additional newline too

            # ERROR HANDLING -> Check if task has enough values
            if len(line) < 3:
                tasks.append(-1) # error code -1

            # ERROR HANDLING -> Check if task has postive integer for [priority] and [CPU burst]
            elif line[1].isnumeric() == False:
                tasks.append(-2) # error code -2

            # Specified that priority should be between 1 and 10
            elif not(1 <= int(line[1]) <= 10):
                tasks.append(-2) # error code -2

            elif line[2].isnumeric() == False:
                tasks.append(-3) # error code -3

            else:
                tasks.append(line) # add tokenised process to list

    return process_obj(tasks) # complete list of tasks


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
