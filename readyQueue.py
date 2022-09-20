#Name: Darragh Hession
#Student Number: 120389806


#I decided to use deque instead of lists as it is much faster
from collections import deque
from process import Process

class ReadyQueue():


    #creates a list containing 8 queues from the class deque and initilaizes the number of processes in the queue to 0
    def __init__(self):
        self._processesInQueue = 0
        self._readyQueue = []

        for queue in range(8):
            queue = deque([])
            self._readyQueue.append(queue)


    def __str__(self):
        string = f"\n{self._processesInQueue} process(es) in queue\n"
        for queue in self._readyQueue:
            string += "["
            for item in queue:
                string += f"{item} ->"
            string += "]\n"
        return string


    """
    Method for adding to the queue. process is an object from the Process class, the number of processes in the queue is increased by one.
    """
    def add(self, process):
        priority = process._priority
        self._readyQueue[priority].append(process)
        self._processesInQueue += 1
        print(f"\n{process} added to queue {priority}\n")
        return

    """
    Method for removing from the queue. queueNumber is the queue from the given priority from the scheduler function. The method uses the deque popleft() method
    in order to efficiently remove from the front of the queue, then the number of processes in the queue is reduced and the the removed process is returned.
    """
    def remove(self, queueNumber):
        toRemove = self._readyQueue[queueNumber]
        process = toRemove.popleft()
        self._processesInQueue -= 1
        print(f"\nCommencing work on {process}")
        return process



if __name__ == "__main__":
    queue = ReadyQueue()
    testProcess1 = Process(1, 32, False, 0, 3, queue)
    testProcess2 = Process(2, 18, False, 0, 6, queue)
    print(queue)
    queue.remove(6)
    print(queue)