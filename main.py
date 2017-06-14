from functions import *

def run():
	foodList = get_foods()
	url = browser(foodList)
	print(get_urls(url))

run()
