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
                print("Could not send slack message:", str(e),
                      'Original message:', message)
        else:
            print("Please provide a slack token, channel and message ")


if __name__ == "__main__":
    slack_token = 'your token'
    channel = '#test'
    message = 'New slackbot saying hi yet again!'
    SlackBot.post_message(slack_token, channel, message)