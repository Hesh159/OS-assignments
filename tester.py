#Name: Darragh Hession
#Student Number: 120389806


from sched import scheduler
from process import Process
from blockedQueue import BlockedQueue
from readyQueue import ReadyQueue
from scheduler import Scheduler


class Tester():

    def test(self):
        print("Initializing test\n")
        blockedQueue = BlockedQueue()
        readyQueue = ReadyQueue()
        scheduler = Scheduler()

        print("Creating processes\n")
        process1 = Process(1, 16, False, 1, readyQueue)
        process2 = Process(2, 256, False, 5, readyQueue)
        process3 = Process(3, 145, True, 4, readyQueue)
        process4 = Process(4, 30, False, 3, readyQueue)
        process5 = Process(5, 8, False, 0, readyQueue)
        process6 = Process(6, 578, True, 6, readyQueue)

        print("Running Scheduler\n")
        scheduler._active = True
        scheduler.scheduler(readyQueue, blockedQueue)


        print("Testing complete")


if __name__ == "__main__":
    tester = Tester()
    tester.test()

