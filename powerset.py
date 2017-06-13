import sqlite3

def powerset(lst):
	x = len(lst)
	output = []
	for i in range(1 << x):
		output.insert(0, [lst[j] for j in range(x) if (i & (1 << j))])
	return output

ingredients = ['lettuce', 'tomato', 'carrot']

a =  powerset(ingredients)

a.sort(key=len)
a.reverse()
a.pop()

for elt in a:
	elt.sort()


conn = sqlite3.connect('database.db')
c = conn.cursor()

def queryfunc(lst):
	for elt in lst:
		strng = ", ".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchone()
