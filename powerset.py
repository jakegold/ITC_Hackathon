import sqlite3

#this function creates a powerset (a list of all possible subsets) from a list
def powerset(lst):
	x = len(lst)
	output = []
	for i in range(1 << x):
		output.insert(0, [lst[j] for j in range(x) if (i & (1 << j))])
	return output

#just an example input - delete this when we get to the real thing
ingredients = ['lettuce', 'tomato', 'carrot']
a =  powerset(ingredients)

#where a is the output of powerset, the following code gets the list of lists into the order we want
a.sort(key=len)
a.reverse()
a.pop()
for elt in a:
	elt.sort()


#start of SQL code
conn = sqlite3.connect('database.db')
c = conn.cursor()

def queryfunc(lst):
	for elt in lst:
		strng = ", ".join(elt)
		c.execute("SELECT URL FROM recipes WHERE Ingredients=?",strng)
		print c.fetchone()
