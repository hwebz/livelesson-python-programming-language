def greeting(name):
	'''
	Greeting function
	'''
	print('Hello ', name)

def add(x, y):
	result = x + y
	return result


x = add(2, 3)
z = add(x=10, y=15)
h = add(y=15, x=10)
j = add(5, y=20)
# v = add(5, x=10) # Error
greeting('Antonio')
help(greeting)

import csv
def porfolio_cost(filename, *, errors='warn'):
	'''
	Computes total shares * price for a CSV file with name, date, shares, price data
	'''

	if errors not in { 'warn', 'silent', 'raise' }:
		raise ValueError('errors must be one of \'warn\', \'silent\', \'raise\'')

	total = 0.0
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for rowno, row in enumerate(rows, start=1):
			try:
				row[2] = int(row[2])
				row[3] = float(row[3])
			except ValueError as err:
			# except Exception as err: # Catches all errors (dangerous)
				if (errors == 'warn'):
					print('Row: ', rowno, 'Bad row: ', row)
					print('Row: ', rowno, 'Reason: ', err)
				elif errors == 'raise':
					raise	# Reraises the last exception
				else:
					pass	# Ignore
				continue # Skip to the next row
			total += row[2] * row[3]
	return total

total = porfolio_cost('porfolio2.csv')
print('Total cost: ', total)

# Loop though all files with the same pattern in name
import glob

total = 0.0
files = glob.glob('porfolio*.csv')
for file in files:
	total += porfolio_cost(file)
print('Total cost: ', total)

# Exception
total = porfolio_cost('missing.csv', errors='silent')
print('Total cost: ',total)

# Functions as Objects
g = greeting
g('John Doe')
items = [10, 20]
items.append(greeting)
items[2]('JimiDARK')

import time
def after(seconds, func):
	time.sleep(seconds)
	func()

# after(5, greeting) # error
names = ['dave', 'Thomas', 'Lewis', 'paula']
names.sort(key=lambda name: name.upper())
a = lambda x: 10*x
a(25)
after(5, lambda: greeting('Jack'))

def add(x, y):
	def do_add():
		print('Adding {} + {} -> {}'.format(x, y, x + y))
		return x + y
	return do_add()

b = add(2, 3) # b now is a function
b() # print text and return the value: 5
after(10, add(2, 3)) # print text and return value because it calls local function inside