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


class InspectionURLTool():
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
            except (urllib.request.URLError, ValueError):
                new_http_response_code = 404
            if website.site_last_http_response != new_http_response_code:
                website.site_last_http_response = new_http_response_code
                website.site_up_status = True if new_http_response_code == 200 else False
                changed_websites.append(website)
        return changed_websites


class InspectionDBTool():
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
        self._started = False
        #self._websites = InspectionDBTool.get_websites()
        self._changed_websites = {}

    def start_scheduled_inspection(self) -> None:
        if not self._started:
            self.job_scheduler.start(10, self._inspection)
            self._slackbot_message_all_startstop()
            self._started = True

    def stop_scheduled_inspection(self) -> None:
        self.job_scheduler.stop()
        self._slackbot_message_all_startstop()

    def add_newly_created_website(self, website):
        status = "UP" if website.site_up_status else "DOWN"
        message = f"{datetime.now()} - Scheduled monitor for {website} initiated, current status: {status}"
        self.slackbot.post_message(website.slack_token, website.slack_channel,
                                   message)

    def remove_website(self, website):
        message = f"{datetime.now()} - Scheduled monitoring for {website} terminated"
        self.slackbot.post_message(website.slack_token, website.slack_channel,
                                   message)

    def _inspection(self) -> None:
        '''schedueld job that runs until stop_scheduled_inspection is called'''
        websites = InspectionDBTool.get_websites()
        self._changed_websites = InspectionURLTool.get_changed_responses(
            websites)
        if len(self._changed_websites) > 0:
            self._slackbot_message_change()
            InspectionDBTool.save_websites(self._changed_websites)
        #else:
        #    self._slackbot_chat(f"{datetime.now()} - No change detected")

    def _slackbot_message_all_startstop(self, start_message=True) -> None:
        for website in InspectionDBTool.get_websites():
            if start_message:
                status = "UP" if website.site_up_status else "DOWN"
                message = f"{datetime.now()} - Scheduled monitor for {website} initiated, current status: {status}"
            else:
                message = f"{datetime.now()} - Scheduled monitoring terminated for {website}"

            if self.slackbot:
                self.slackbot.post_message(website.slack_token,
                                           website.slack_channel, message)
            else:
                print(message)

    def _slackbot_message_change(self) -> None:
        for website in self._changed_websites:
            status = "UP" if website.site_up_status else "DOWN"
            message = f"{datetime.now()} - {website} is {status}"
            if self.slackbot:
                self.slackbot.post_message(website.slack_token,
                                           website.slack_channel, message)
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
    slack_bot = SlackBot
    #slack_bot = None
    inspector = Inspector(job_scheduler, slack_bot)
    inspector.start_scheduled_inspection()

    new_dummy_website = Website(
        site_name='new_dummy_website',
        site_url='https://new_dummy_website/',
        slack_token='xoxb-2564298031248-2533960760054-Iw1MZuJHR8CbwMyvZf2jx5NX',
        slack_channel='#test')

    inspector.add_newly_created_website(new_dummy_website)
    inspector.remove_website(new_dummy_website)
    #test multiple starts
    inspector.start_scheduled_inspection()
    inspector.start_scheduled_inspection()
    time.sleep(120)
    inspector.stop_scheduled_inspection()

    print_websites()
