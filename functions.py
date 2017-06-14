from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from os import listdir
from os.path import isfile, join
import webbrowser

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

def browser(lst):
	string = "%20".join(lst)
	url = 'http://allrecipes.com/search/results/?wt='+string+'&sort=re'
	webbrowser.open(url)	

def get_urls(url):
	html = ''
	try:
		response = urlopen(url)
		html = response.read()
		findLinks = GetLinks(html)
	except Exception:
		print ("Can't crawl that page")
		return list()
	return findLinks.get_links()
