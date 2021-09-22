import urllib.request


class URLStatus():
    """Check a url's status with the is_alive static command"""
    @staticmethod
    def is_alive(url: str) -> bool:
        '''Return true if a website is up and running'''
        try:
            #retval = (urllib.request.urlopen("http://foo.example.org/").getcode())
            http_retval = (urllib.request.urlopen(url).getcode())
            if http_retval == 200:
                return True
            else:
                return False
        except:
            http_retval = 404
            return False


if __name__ == "__main__":
    status = URLStatus.is_alive("https://www.stackoverflow.com")
    print(f'https://www.stackoverflow.com: {status}')
    status = URLStatus.is_alive("http://foo.example.org/")
    print(f'http://foo.example.org/: {status}')