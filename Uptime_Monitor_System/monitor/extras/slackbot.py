from slack import WebClient
from slack.errors import SlackApiError
import os
from os.path import join, dirname
from dotenv import load_dotenv


class SlackBot():
    """Slack messagin bot - Every instance is tied to a channel. Create a slack_token and a channel then use it to create a SlackBot"""
    def __init__(self, channel: str) -> None:
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        token = os.environ.get('SLACK_TOKEN')
        self._client = WebClient(token)
        self.channel = channel
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


if __name__ == "__main__":
    bot = SlackBot(channel="#uptime-monitor-system")
    if bot.post_message(message='OOP class message again!'):
        print("Message sent!")
    else:
        print("Message failed", bot.last_error)
