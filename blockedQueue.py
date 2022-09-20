#Name: Darragh Hession
#Student Number: 120389806


#I decided to use deque instead of lists as it is much faster
from collections import deque


class BlockedQueue():

    #initializes the blocked queue using the deque class
    def __init__(self):
        self._blockedQueue = deque([])
        self._processesInQueue = 0

    #prints a string representation of the queue
    def __str__(self):
        string = f"\n {self._processesInQueue} process(es) in queue \n["
        for item in self._blockedQueue:
            string += f" {item} ->"
        string += "]"
        return string

    #simple add method adds the process to the end of the blocked queue
    def add(self, process):
        self._blockedQueue.append(process)    
        self._processesInQueue += 1
        print(f"\n{process} added to blocked queue")
        return

    #simple remove method removes the process at the front of the queue
    def remove(self):
        process = self._blockedQueue.popleft()
        self._processesInQueue -= 1
        print(f"\nI/O on {process} has been completed.")
        return process


if __name__ == "__main__":
    testQueue = BlockedQueue()
    testQueue.add(1)
    testQueue.add(5)
    testQueue.add(7)
    print(testQueue)
    testQueue.remove()
    print(testQueue)