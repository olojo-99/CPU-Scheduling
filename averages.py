#!/usr/bin/env python3

# Calculate the average wait time for processes scheduled using algorithm
def average_wait(processes):
    total_wait = 0

    # total time spent in wait queue -> wait time = turnaround time - CPU burst time
    for i in range(len(processes)):
        total_wait += processes[i].turnaround - processes[i].burst

    return '{:.2f}'.format(total_wait / len(processes)) # calculated average to 2 decimal places


# Average interval from the time of submission of a process/task to the time of completion
def average_turnaround(processes):
    total_turnaround = 0

    # add CPU burst times of all but last process in list
    for i in range(len(processes)):
        total_turnaround += processes[i].turnaround

    return '{:.2f}'.format(total_turnaround / len(processes)) # calculated average to 2 decimal places


# Print details on processes after running
def process_details(processes):
    for task in processes:
        print(f"Process ({task.name}) arrived at time (0) and ran for ({task.burst}) MS. It had a turn-around time of ({task.turnaround})\n")

# Print details on averages
def avg_details(processes):
    print(f"The average waiting time was: {average_wait(processes)}")
    print(f"The average turnaround time was: {average_turnaround(processes)}")


'''
I certify that this assignment is my own work carried out in a manner pursuant to the DCU Academic Integrity Policy,
based on my personal study and/or research and that I have acknowledged all material and sources used in its preparation.
Benjamin Olojo - 19500599
'''
