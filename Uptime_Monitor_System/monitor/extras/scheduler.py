import threading
import datetime


class Scheduler:
    """A hardcoded & threaded scheduler. Define a job in self__scheduled_job() and 
    use .start() to start a infinte recursive job"""
    def __init__(self) -> None:
        self.__lock = threading.Lock()
        self.__started = False

    def start(self, secconds) -> None:
        '''start the job'''
        if not self.__started:
            self.__started = True
            self.secconds = secconds
            threading.Thread(target=self.__scheduled_worker).start()
        else:
            raise InterruptedError('You can only start the scheduler once')

    def __scheduled_worker(self):
        '''define a recursive job'''
        with self.__lock:
            print(f"{datetime.datetime.now()}: Worker: I'm working...")
            threading.Timer(self.secconds, self.__scheduled_worker).start()


if __name__ == '__main__':
    import time
    scheduler = Scheduler()
    scheduler.start(1)
    print("__main__: After the worker started: I can still run!")
    time.sleep(3)
    print("__main__: After the worker started: and run some more!")
    scheduler.start(10)