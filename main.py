from functions import *

def run():
	# foodList = get_foods()
	foodList = ['chicken', 'cucumber', 'onion', 'pumpkin', 'tomato']
	url = browser(foodList)
	urls = get_urls(url)
	for url in urls:
		print(url)
		print(get_ingreds(url))

run()
