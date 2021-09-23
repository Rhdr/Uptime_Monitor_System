import threading


class JobScheduler:
    """A threaded scheduler that can perform a predifined function/job. 
    use .start() to start a infinte recursive job"""
    def __init__(self) -> None:
        self.__lock = threading.Lock()
        self.__started = False

    def start(self, seconds, function_to_run) -> None:
        '''run the fucntion/job every x seconds'''
        if not self.__started:
            self.__started = True
            self.seconds = seconds
            self.function_to_run = function_to_run
            threading.Thread(target=self.__scheduled_worker).start()
        else:
            raise InterruptedError('You can only start the JobScheduler once')

    def __scheduled_worker(self) -> None:
        '''define a recursive job'''
        with self.__lock:
            # print(f"{datetime.datetime.now()}: Worker: I'm working...")
            self.function_to_run()
            threading.Timer(self.seconds, self.__scheduled_worker).start()


if __name__ == '__main__':
    import datetime
    import time

    def job_that_needs_doing():
        print(f"{datetime.datetime.now()}: Someone is doing the job!")

    scheduler = JobScheduler()
    scheduler.start(1, job_that_needs_doing)
    print("__main__: After the worker started: I can still run!")
    time.sleep(3)
    print("__main__: After the worker started: and run some more!")
    print("__main__: After the worker started: Lets run the worker again!")
    scheduler.start(10, job_that_needs_doing)