from bs4 import BeautifulSoup

class GetLinks():

    def __init__(self, html):
        super().__init__()
        self.soup = BeautifulSoup(html, 'html.parser')
        self.links = set()
        self.ingredients = list()

#   Gets the links from the url
    def get_links(self):
        self.page_links()
        return self.links
    
#   Gets the next 3 recipes
    def page_links(self):
        substring = '/recipe/'
        for link in self.soup.find_all('a'):
            next = link.get('href')
            if next != None:
                if substring in next and len(self.links) < 3:
                    next = 'http://allrecipes.com/' + next
                    self.links.add(next)
                    
#   Returns a list of all ingredients needed
    def get_ingredients(self):
        self.page_ingredients()
        return self.ingredients
        
#   Gets the list of ingredients from a url      
    def page_ingredients(self):
        for link in self.soup.find_all('span', {'class':'recipe-ingred_txt added'}):
            next = link.get_text()
            self.ingredients.append(next)
