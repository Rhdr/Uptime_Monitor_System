import urllib.request
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

    def _inspection_job(self, url_list) -> None:
        new_inspection_job_report = (
            URLInspectTool.urlopen_http_response(url_list))
        if self.prev_inspection_job_report != new_inspection_job_report:
            print("status changed detected!", new_inspection_job_report)
        else:
            print("all is well, no status changed detected")
        self.prev_inspection_job_report = new_inspection_job_report

    def _slack_chat(self) -> None:
        pass

    def _db_update(self) -> None:
        pass


if __name__ == "__main__":
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

    sinspector = ScheduledURLInspector(urls, job_scheduler, slackbot)
    sinspector.start_scheduled_inspection()