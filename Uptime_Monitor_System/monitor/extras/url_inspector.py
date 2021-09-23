import urllib.request


class URLInspector():
    """Check a url's status with the is_alive static command"""
    def __init__(self) -> None:
        self.last_http_response = None

    def is_alive(self, url: str) -> bool:
        '''Return true if a website is up and running'''
        try:
            #retval = (urllib.request.urlopen("http://foo.example.org/").getcode())
            self.last_http_response = (urllib.request.urlopen(url).getcode())
            if self.last_http_response == 200:
                return True
            else:
                return False
        except:
            self.last_http_response = 404
            return False


if __name__ == "__main__":
    url_status = URLInspector()
    status = url_status.is_alive("https://www.stackoverflow.com")
    print(f'https://www.stackoverflow.com: {status}')
    status = url_status.is_alive("http://foo.example.org/")
    print(f'http://foo.example.org/: {status}')
    status = url_status.is_alive("https://www.google.com/")
    print(f'https://www.google.com: {status}')
    print(url_status.last_http_response)
    print(f'neverssl.com/: {status}')
    print(url_status.last_http_response)