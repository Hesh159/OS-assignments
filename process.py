#Name: Darragh Hession
#Student Number: 120389806


class Process():

    """
    The id attribute only exists in order to track the process when testing.
    executionDuration is a positive integer referring to the number of CPU time quanta required to complete.
    inputOutput is a boolean determining whether or not the process has I/O.
    priority refers to the original priority given to the process.  
    The queue method is called upon initialization to automatically place the process in the appropriate queue.
    """
    def __init__(self, id, executionDuration, inputOutput, priority, queue):
        self._id = id
        self._executionDuration = executionDuration
        self._inputOutput = inputOutput
        self._priority = priority
        self.queue(queue)
    


    #simple string method implemented for testing purposes
    def __str__(self):
        return f"Process {self._id}"
    


    """
    Method for simulating running the process.
    timeslice is the current timeslice for the priority of the process as determined by the scheduler.
    Method removes the timeSlice from the current execution duration and returns the remaining execution duration time.
    """
    def run(self, timeSlice):
        self._executionDuration -= timeSlice
        return self._executionDuration


    """
    Method for adding the process to the ready queue. This method is called upon initialization of the process.
    """
    def queue(self, queue):
        if queue != None:
            queue.add(self)
        return


if __name__ == "__main__":
    testProcess = Process(1, 32, False, 3, None)
    print(testProcess)
    testProcess.run(15)
    print(testProcess._executionDuration)



