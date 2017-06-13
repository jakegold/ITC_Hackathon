import sqlite3

# def queryfunc(lst):
# 	conn = sqlite3.connect('database.db')
# 	c = conn.cursor()
# 	for element in lst:
# 		strng = ", ".join(element)
# 		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
# 		print c.fetchall()
def queryfunc(lst):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	for elt in lst:
		strng = "%".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients LIKE %?%",strng)
		print c.fetchall()
