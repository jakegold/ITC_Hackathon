from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from os import listdir
from os.path import isfile, join
import webbrowser
from urllib.request import urlopen
import smtplib
from get_links import GetLinks
from bs4 import BeautifulSoup

app = ClarifaiApp()

# Returns a set of all the ingredients in the fridge
def get_foods():
	filepath = 'fridge_pics'
	files = get_all_files(filepath)
	foodList = []
	for pic in files:
		if pic[0] == '.':
			continue
		newFilepath = filepath + '/' + pic
		image = [newFilepath]
		img = app.tag_files(image, model='food-items-v1.0')
		foodItem = (img["outputs"][0]['data']['concepts'][0]['name'])
		foodList.append(foodItem)
	return foodList

# Returns all of the files from a datapath
def get_all_files(filepath):
	all_files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
	return all_files

# Creates a powerset (a list of all possible subsets) from a list
def power_set(elements):
	x = len(elements)
	result = []
	for i in range(1 << x):
		result.insert(0, [elements[j] for j in range(x) if (i & (1 << j))])
	result.sort(key=len)
	result.reverse()
	result.pop()
	for element in result:
		if (len(element) > 5):
			result.remove(element)
	return result

# Returns the url of the searched food list
def browser(lst):
	string = "%20".join(lst)
	url = 'http://allrecipes.com/search/results/?wt='+string+'&sort=re'
# 	webbrowser.open(url)
	return url

# Builds a soup object and returns it
def build_soup(url):
	html = ''
	response = urlopen(url)
	html = response.read()
	findLinks = GetLinks(html)
	return findLinks

# Returns a list of the top recipes from the list of foods
def get_urls(url):
	findLinks = build_soup(url)
	return findLinks.get_links()

# Gets a list of ingredients that are needed for a recipe
def get_ingreds(url):
	findLinks = build_soup(url)
	return findLinks.get_ingredients()

#Returns the title of a URL
def extract_html_title(url):
	html = ''
	response = urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup.title.text

# Returns shopping list
def what_2_buy(fridgefoods, ingredients):
	shoppingList = ingredients[:]
	for ing in ingredients:
		for item in fridgefoods:
			if item in ing:
				shoppingList.remove(ing)
				break
		continue
	return shoppingList

# Sends the email
def send_email(to_address, msg):
    subject = "Recommended Recipes"
    register = '\N{REGISTERED SIGN}'
    if register in msg:
    	msg = msg.replace('\N{REGISTERED SIGN}', '')
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = 'itcsmartfridge@gmail.com'
    mail.login(sender, 'iamafridge')
    mail.sendmail(sender, to_address, message)
    mail.close()
