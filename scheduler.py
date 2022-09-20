#Name: Darragh Hession
#Student Number: 120389806

from process import Process
from readyQueue import ReadyQueue

class Scheduler():
    
    def __init__(self):
        self._active = False


    """
    Method for the scheduler algorithm. The inputs are the readyqueue and the blockedqueue
    First the algorithm initiates the savedCpuTime variable. If a process terminates, savedCpuTime becomes the remainder of the time slice, if a process uses its 
    entire time slice this variable becomes 0. It is added to the time slice of the next process.

    Next the algorithm checks if it should go into low power mode (2 or less processes ready)

    Now the algorithm loops through the queues searching for processes, if found, and if the process has no I/O the process is removed
    from the queue and ran using the run method. If it is completed, a message is printed and savedCpuTime is updated, else it is added to a lower priority queue and
    the loop continues.

    If the process has I/O it is added to the blockedQueue, for this simulation I decided that I/O will be "completed" when the system is set to low power mode

    Finally, if the loop reaches the final queue containing the idle process, the system is set to sleep
    """
    def scheduler(self, readyQueue, blockedQueue):

        savedCpuTime = 0
        while self._active != False:
            
            #if there are 2 or less processes in the queue, the system switches to lower power mode and the quanta is increased.
            if readyQueue._processesInQueue > 2:
                quanta = 1
            else:
                quanta = 2
                if blockedQueue._processesInQueue != 0:
                    process = blockedQueue.remove()
                    readyQueue.add(process)

            for queuePriority, queue in enumerate(readyQueue._readyQueue):

                if len(queue) != 0:
                    if queuePriority != len(readyQueue._readyQueue) - 1:

                        process = readyQueue.remove(queuePriority)
                        timeSlice = (quanta * (2 ** queuePriority)) + savedCpuTime

                        if process._inputOutput == True:
                            process._inputOutput = False
                            process._priority -= 1
                            blockedQueue._blockedQueue.append(process)
                            

                        runResult = process.run(timeSlice)
                        if runResult < 0:
                            print(f"\n{process} terminated with {runResult * -1} time remaining in the time slice")
                            print(f"\n{process} completed")
                            savedCpuTime = runResult * -1
                            continue
                        else:
                            savedCpuTime = 0
                            if queuePriority != 6:  #if process is at priority 6 it can not be placed any lower.
                                process._priority += 1
                                readyQueue.add(process)
                                continue
                            else:
                                readyQueue.add(process)
                                continue
            
            if readyQueue._processesInQueue == 0:
                self._active = False
