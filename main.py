from functions import *

def run():
	# foodList = get_foods()
	foodList = ['pineapple', 'cucumber', 'tomato']
	url = browser(foodList)
	urls = get_urls(url)
	email = 'Hello! Here are some options for dinner tonight:' + '\n' + '\n'
	for url in urls:
		email += extract_html_title(url) + '\n' + url + '\n'
		ingred_list = get_ingreds(url)
		shopping_list = what_2_buy(foodList, ingred_list)
		email += ', \n'.join(shopping_list)
		email += '\n \n'
	email += 'Enjoy your dinner! \n Love, \n Your Smart Fridge'
	send_email('roybot23@gmail.com', email)


run()
