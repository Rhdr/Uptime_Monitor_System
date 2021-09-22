from slack import WebClient
from slack.errors import SlackApiError


class SlackBot():
    """Slack messagin bot - Every instance is tied to a channel. Create a slack_token and a channel then use it to create a SlackBot"""
    def __init__(self, slack_token: str, channel: str) -> None:
        self.__slack_token = slack_token
        self.channel = channel
        self.client = WebClient(token=slack_token)

    def post_message(self, message: str) -> bool:
        '''Post a message to slack to a hardcoded channel'''
        try:
            response = self.client.chat_postMessage(channel=self.channel,
                                                    text=message)
            return True
        except SlackApiError as e:
            assert e.response[
                "error"]  # str like 'invalid_auth', 'channel_not_found'
            return False


if __name__ == "__main__":
    bot = SlackBot(
        slack_token="xoxb-2503398942439-2525293310900-87ve4GJrP2hkmaTcHhuopgvG",
        channel="#uptime-monitor-system")
    if bot.post_message(message='OOP class message again!'):
        print("Message sent!")
    else:
        print("Message failed")
