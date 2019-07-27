import threading
from time import sleep
from sys import stdout


class Process():
    """
    A class that creates a process and a loading screen for the process
    """

    def __init__(self, total_time=10000):
        """
        Parameters
        ----------
        total_time : int, optional
            The total amount of time taken by this process (default is 10000)
        """
        self.progress = 0
        self.isDone = False
        self.total_time = total_time

    def do_work(self):
        """
        Creates loop for total_time
        """
        self.isDone = 0
        for i in range(self.total_time):
            self.progress = i
            sleep(0.001)
        self.isDone = True

    def get_progress(self):
        """
        Getter for progress

        Returns int
        """
        return self.progress

    def loading_animation(self):
        """
        Creates loading animation
        """
        while not self.isDone:
            chars = r'/—\|'  # Character set for loading symbol

            # Update loading graphic
            for char in chars:
                progress = round(self.get_progress() / self.total_time * 100)
                stdout.write(f'\rLoading {char} {progress}%')
                sleep(.1)
                # Flush to ensure accurate output
                stdout.flush()


# Instantiate process
worker = Process(1000)

# Start the work in a new thread
workThread = threading.Thread(target=worker.do_work)
workThread.start()

worker.loading_animation()


print('\nDone')
