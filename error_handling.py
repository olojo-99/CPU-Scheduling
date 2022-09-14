#!/usr/bin/env python3

import sys
import os.path

'''
Error Codes:
    -1 = Not enough values (missing name, priority, burst)
    -2 = Invalid priority number (not in range 1-10 -> From assignment spec)
    -3 = Invalid CPU burst (not >= 0)
'''

# Function will validate each process that is passed to it
# Process will be an error code mentioned above if invalid
# In the case of an erroneus process, prints appropriate error message and returns 1
# Returns 0 if process is valid
def proc_error(process, line):
    if process == -1:
        print(f"* Process on line {line} doesn't have enough values *\n")
        return 1

    elif process == -2:
        print(f"* Process on line {line} has a [priority] that isn't between 1-10 *\n")
        return 1

    elif process == -3:
        print(f"* Process on line {line} has a [CPU burst] that isn't a positive integer *\n")
        return 1

    # In the case of no errors
    return 0


# Function to if a valid file was provided
# File must also exist
def file_error(args):
    # Program will exit with error message if a valid file was not provided
    if len(args) < 2:
        exit("-> Not enough command line arguments provided [File required]")

    elif not(os.path.isfile(args[1])): # [1]
        exit("-> File provided does not exist")


# [1] linuxize.com. How to Check if a File or Directory Exists in Python [Online]. Available: https://linuxize.com/post/python-check-if-file-exists/


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
