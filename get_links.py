from html.parser import HTMLParser
from urllib import parse

class GetLinks(HTMLParser):

    def __init__(self, home_url, page_url):
        super().__init__()
        self.home_url = home_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    substr = '/recipe/'
                    if substr in value:
                        url = parse.urljoin(self.home_url, value)
                        self.links.add(url)
                        break

    def page_links(self):
        return self.links

    def error(self, message):
        pass
