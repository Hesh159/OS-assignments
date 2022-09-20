# OS-assignments
A collection of my operating system assingments.

The first one is a simple cpu scheduler made in python. It recieves processes, and places them into the queue depending on the processes priority. 
The scheduler determines the amount of time it should dedicate to each process depending on its priority with more time dedicated to lower priority processes.
The scheduler then "works" on the first process in queue for the specified amount of time. If the process is finished the scheduler moves on, using the remaining time
in the next time slice. If the process is not finished, it drops down in priority if possible, and is sent to the back of the queue. If the process has a required
I/O, the process is blocked for the time being and sent to the blocked queue while the scheduler moves on. If the scheduler has 2 or less processes in the queue, 
it enters "low power mode", and will spend more time on each process.
