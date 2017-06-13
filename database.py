import sqlite3

#start of SQL code
conn = sqlite3.connect('database.db')
c = conn.cursor()

def queryfunc(lst):
	for elt in lst:
		strng = ", ".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchall()
