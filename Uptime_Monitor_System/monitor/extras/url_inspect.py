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


if __name__ == "__main__":
    #url_inspect_tool = URLInspectTool()
    urls = [
        "https://www.google.com/",
        "https://www.foo.bar.com/",
        "https://www.stackoverflow.com",
    ]
    print(URLInspectTool.urlopen_http_response(urls))
