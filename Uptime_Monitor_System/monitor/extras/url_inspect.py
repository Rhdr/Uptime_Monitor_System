import urllib.request
from datetime import datetime

from django.db.models.query import QuerySet

if __name__ == '__main__':
    import sys
    sys.path.insert(
        1, 'c:\\Projects\\Uptime_Monitor_System\\Uptime_Monitor_System')
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "Uptime_Monitor_System.settings")
    import django
    django.setup()
    from django.core.management import call_command

    from monitor.extras.job_scheduler import JobScheduler
    from monitor.extras.slackbot import SlackBot
    from monitor.models import Website
else:
    from .job_scheduler import JobScheduler
    from .slackbot import SlackBot
    from ..models import Website


class inspectionURLTool():
    """Get a http response form websites & temp store result back into the website obj
    The website obj needs to be saved to persist the data"""
    @staticmethod
    def get_changed_responses(websites: list) -> dict:
        '''Return a dict containing the url:http_response_codes'''
        changed_websites = []
        for website in websites:
            try:
                new_http_response_code = urllib.request.urlopen(
                    website.site_url).getcode()
            except urllib.request.URLError:
                new_http_response_code = 404
            if website.site_last_http_response != new_http_response_code:
                website.site_last_http_response = new_http_response_code
                website.site_up_status = True if new_http_response_code == 200 else False
                changed_websites.append(website)
        return changed_websites


class inspectionDBTool():
    """Get & Save websites"""
    @staticmethod
    def save_websites(websites: list) -> bool:
        for website in websites:
            website.save()

    @staticmethod
    def get_websites() -> dict:
        #websites = Website.objects.in_bulk(field_name='site_url')
        websites = list(Website.objects.all())
        return websites


class Inspector:
    """This class makes use of the JobScheduler to schedule 'website inspections'. 
    Then using the URLInspectTool, it gets the status of the inspected websites.
    Next Slackbot is used to post/chat website status changes to slack
    Lastly InspectDBUpdater is used to update any status change to the db"""
    def __init__(self, job_scheduler: JobScheduler,
                 slackbot: SlackBot) -> None:
        self.job_scheduler = job_scheduler
        self.slackbot = slackbot
        self.websites = inspectionDBTool.get_websites()

    def start_scheduled_inspection(self) -> None:
        self.job_scheduler.start(5, self._inspection)
        self._slackbot_chat(
            f"{datetime.now()} - Scheduled inspection started, monitoring the following websites: {self.websites}"
        )

    def stop_scheduled_inspection(self) -> None:
        self.job_scheduler.stop()
        self._slackbot_chat(
            f"{datetime.now()} - Scheduled inspections stopped, the websites are no longer being monitored"
        )

    def _inspection(self) -> None:
        '''schedueld job that runs until stop_scheduled_inspection is called'''
        changed_websites = inspectionURLTool.get_changed_responses(
            self.websites)
        if len(changed_websites) > 0:
            self._slackbot_chat(
                f"{datetime.now()} - A status change have been detected! {changed_websites}"
            )
            inspectionDBTool.save_websites(changed_websites)
        else:
            self._slackbot_chat(
                f"{datetime.now()} - All is well, no change detected")

    def _slackbot_chat(self, message) -> None:
        if self.slackbot:
            self.slackbot.post_message(message)
        else:
            print(message)


if __name__ == "__main__":
    import time

    def print_websites():
        websites = Website.objects.all()
        for website in websites:
            print(website.site_name, website.site_url,
                  website.site_last_http_response)

    print('Start')
    print_websites()
    print('')

    job_scheduler = JobScheduler()
    # slack_bot = SlackBot
    slack_bot = None
    inspector = Inspector(job_scheduler, slack_bot)
    inspector.start_scheduled_inspection()
    time.sleep(60)
    inspector.stop_scheduled_inspection()

    print_websites()
