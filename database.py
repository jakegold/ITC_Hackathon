import sqlite3

def queryfunc(lst):
	conn = sqlite3.connect('database.db')
	c = conn.cursor()
	for element in lst:
		strng = ", ".join(element)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchall()
