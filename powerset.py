import sqlite3

#this function creates a powerset (a list of all possible subsets) from a list
def powerset(lst):
	x = len(lst)
	output = []
	for i in range(1 << x):
		output.insert(0, [lst[j] for j in range(x) if (i & (1 << j))])
	output.sort(key=len)
	output.reverse()
	output.pop()
	for elt in output:
		elt.sort()
	return output


#start of SQL code
conn = sqlite3.connect('database.db')
c = conn.cursor()

def queryfunc(lst):
	for elt in lst:
		strng = ", ".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchall()
