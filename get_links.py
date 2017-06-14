from bs4 import BeautifulSoup

class GetLinks():

    def __init__(self, html):
        super().__init__()
        self.soup = BeautifulSoup(html, 'html.parser')
        self.links = set()

    def get_links(self):
        self.page_links()
        return self.links

    def page_links(self):
        substring = '/recipe/'
        for link in self.soup.find_all('a'):
            next = link.get('href')
            if next != None:
                if substring in next and len(self.links) < 3:
                    next = 'http://allrecipes.com/' + next
                    self.links.add(next)
