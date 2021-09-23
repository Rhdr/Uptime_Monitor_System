import threading


class JobScheduler:
    """A threaded scheduler that can perform a predifined function/job. 
    use .start() to start a infinte recursive job"""
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._started = False

    def start(self, seconds: int, job, **job_kwargs) -> None:
        '''run the fucntion/job every x seconds'''
        if not self._started:
            self._started = True
            self.seconds = seconds
            self.job = job
            self.job_kwargs = job_kwargs
            threading.Thread(target=self._scheduled_worker).start()
        else:
            raise InterruptedError('You can only start the JobScheduler once')

    def _scheduled_worker(self) -> None:
        '''define a recursive job'''
        with self._lock:
            # print(f"{datetime.datetime.now()}: Worker: I'm working...")
            self.job(**self.job_kwargs)
            threading.Timer(self.seconds, self._scheduled_worker).start()


if __name__ == '__main__':
    import datetime
    import time

    def job_that_needs_doing(message='working'):
        print(f"{datetime.datetime.now()}: {message}")

    scheduler = JobScheduler()
    scheduler.start(3,
                    job_that_needs_doing,
                    message="Someone is doing the job!")
    print("__main__: After the worker started: I can still run!")
    time.sleep(7)
    print("__main__: After the worker started: and run some more!")
    print("__main__: After the worker started: Lets run the worker again!")
    scheduler.start(10, job_that_needs_doing)