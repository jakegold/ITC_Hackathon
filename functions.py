from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

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
