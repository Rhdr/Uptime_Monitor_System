from slack import WebClient
from slack.errors import SlackApiError
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests


class SlackBot_old():
    """Slack messagin bot - Every instance is tied to a channel. Create a slack_token and a channel then use it to create a SlackBot"""
    def __init__(self, channel="#uptime-monitor-system") -> None:
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        token = os.environ.get('SLACK_TOKEN')
        self._client = WebClient(token)
        self.channel = "#uptime-monitor-system"
        self.last_error = None

    def post_message(self, message: str) -> bool:
        '''Post a message to slack to a hardcoded channel'''
        try:
            response = self._client.chat_postMessage(channel=self.channel,
                                                     text=message)
            self.last_error = None
            return True
        except SlackApiError as e:
            assert e.response[
                "error"]  # str like 'invalid_auth', 'channel_not_found'
            self.last_error = e.response
            return False


class SlackBot():
    @staticmethod
    def post_message(slack_token: str, slack_channel: str,
                     message: str) -> None:
        if slack_token and slack_channel and message:
            data = {
                'token': slack_token,
                'channel': slack_channel,  # User ID. 
                'as_user': True,
                'text': message
            }
            try:
                requests.post(url='https://slack.com/api/chat.postMessage',
                              data=data)
            except Exception as e:
                print("Could not send slack message:", str(e))
        else:
            print("Please provide a slack token, channel and message ")


if __name__ == "__main__":
    slack_token = "xoxb-2503398942439-2525293310900-lHr4bEhHNbg0bgnafakqpSod"
    #slack_token = ""
    channel = '#monitor'
    message = 'New slackbot saying hi yet again!'
    SlackBot.post_message(slack_token, channel, message)

    # bot = SlackBot()
    # if bot.post_message(message='OOP class message again!'):
    #     print("Message sent!")
    # else:
    #     print("Message failed", bot.last_error)
