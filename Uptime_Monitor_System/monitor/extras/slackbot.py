from slack import WebClient
from slack.errors import SlackApiError
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests


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
