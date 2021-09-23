import urllib.request
from datetime import datetime
from job_scheduler import JobScheduler
from slackbot import SlackBot


class URLInspectTool():
    """Get a httpresponse form a url list"""
    @staticmethod
    def urlopen_http_response(url_list: list) -> dict:
        '''Return a dict containing the url:http_response_codes'''

        retdict = {}
        for url in url_list:
            try:
                http_response_code = (urllib.request.urlopen(url).getcode())
            except urllib.request.URLError:
                http_response_code = 404
            retdict[url] = http_response_code
        return retdict


class ScheduledURLInspector:
    def __init__(self, url_list: list, job_scheduler: JobScheduler,
                 slackbot: SlackBot) -> None:
        self.url_list = url_list
        self.job_scheduler = job_scheduler
        self.slackbot = slackbot
        self.prev_inspection_job_report = {}

    def start_scheduled_inspection(self) -> None:
        self.job_scheduler.start(5,
                                 self._inspection_job,
                                 url_list=self.url_list)
        self._slackbot_chat(
            f"{datetime.now()} - Scheduled inspection started, monitoring the following websites: {self.url_list}"
        )

    def stop_scheduled_inspection(self):
        self.job_scheduler.stop()
        self._slackbot_chat(f"{datetime.now()} - Scheduled inspections stopped, the websites are no longer being monitored")

    def _inspection_job(self, url_list) -> None:
        new_inspection_job_report = (
            URLInspectTool.urlopen_http_response(url_list))
        if self.prev_inspection_job_report != new_inspection_job_report:
            self._slackbot_chat(
                f"{datetime.now()} - A status change have been detected! {new_inspection_job_report}")
        else:
            self._slackbot_chat(f"{datetime.now()} - All is well, no change detected")
        self.prev_inspection_job_report = new_inspection_job_report


    def _slackbot_chat(self, message) -> None:
        if slackbot:
            self.slackbot.post_message(message)
        else:
            print(message)

    def _db_update(self) -> None:
        pass


if __name__ == "__main__":
    import time

    #url_inspect_tool = URLInspectTool()
    urls = [
        "https://www.google.com/",
        "https://www.foo.bar.com/",
        "https://www.stackoverflow.com",
    ]
    print(URLInspectTool.urlopen_http_response(urls))

    print('')
    print('ScheduledURLInspector')

    job_scheduler = JobScheduler()
    slackbot = SlackBot()
    #slackbot = None

    sinspector = ScheduledURLInspector(urls, job_scheduler, slackbot)
    sinspector.start_scheduled_inspection()
    time.sleep(20)
    sinspector.stop_scheduled_inspection()