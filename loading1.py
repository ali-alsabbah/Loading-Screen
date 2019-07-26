import threading
from time import sleep


class ClassWithLongProcess():

    def __init__(self):
        self.progress = 0
        self.isDone = False

    def doWork(self):
        self.isDone = 0
        for i in range(10000):
            self.progress = i
            sleep(0.001)
        self.isDone = True

    def getProgress(self):
        return self.progress


worker = ClassWithLongProcess()

# Start the work in a new thread
workThread = threading.Thread(target=worker.doWork)
workThread.start()

while not worker.isDone:
    sleep(1)
    print('%s of 10000' % worker.getProgress())

print('Done')
