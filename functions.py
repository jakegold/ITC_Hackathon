from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from os import listdir
from os.path import isfile, join
import sqlite3

app = ClarifaiApp()

# Returns a set of all the ingredients in the fridge
def get_foods():
	filepath = 'fridge_pics'
	files = get_all_files(filepath)
	foodList = []
	for pic in files:
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
	for elt in result:
		elt.sort()
	return result

# Returns a list of urls for the recipes
def queryfunc(lst):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	result = []
	for elt in lst:
		strng = "%".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients LIKE %?%",strng)
		result.append(c.fetchall())
	return result
