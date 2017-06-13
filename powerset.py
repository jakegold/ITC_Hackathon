import sqlite3

# c.execute("INSERT INTO recipes (ID, Ingredients, URL) VALUES (3, \"test2\", \"test2\")")
# conn.commit()


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

print a


conn = sqlite3.connect('database.db')
c = conn.cursor()

def queryfunc(lst):
	for elt in lst:
		strng = ", ".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchone()