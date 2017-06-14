from html.parser import HTMLParser
from urllib import parse

class GetLinks(HTMLParser):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    substr = '/recipe/'
                    if substr in value:
                        url = parse.urljoin(self.home_url, value)
                        if len(links) < 4:
                            self.links.add(url)
                        break

    def page_links(self):
        return self.links

    def error(self, message):
        passge
