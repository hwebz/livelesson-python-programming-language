import csv

def read_porfolio(filename, *, errors='warn'):
	'''
	Read a CSV file with name, date, shares, price data into a list
	'''
	if errors not in { 'warn', 'silent', 'raise' }:
		raise ValueError('errors must be one of \'warn\', \'silent\', \'raise\'')

	porfolio = [] # List of records
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
			#record = tuple(row)
			record = {
				'name': row[0],
				'date': row[1],
				'shares': row[2],
				'price': row[3],
			}
			porfolio.append(record)
	return porfolio

porfolio = read_porfolio('porfolio2.csv')
print(porfolio)

total = 0.0
# for name, date, shares, price in porfolio:
# 	total += shares * price # Shares * Price

for holding in porfolio:
	total += holding['shares'] * holding['price']

print('Total cost: ', total)

import json
data = json.dumps(porfolio)
print(data)
port = json.loads(data)
print(port)

names = []
more100 = []
for holding in porfolio:
	names.append(holding['name'])
	if holding['shares'] > 50:
		more100.append(holding)

total = sum([holding['shares'] * holding['price'] for holding in porfolio])
names = [holding['name'] for holding in porfolio]
more100 = [holding for holding in porfolio if holding['shares'] > 50]
unique_names = set(names)
# unique_names = {holding['name'] for holding in portfolio}
namestr = ','.join(unique_names)

import urllib.request
u = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
data = u.read()
print(data)                                                                                    
pricedata = data.split()
for name, price in zip(unique_names, pricedata):
	print(name, ' = ', price)

prices = dict(zip(unique_names, pricedata))
print(prices['AA']*50) # Repeat string
prices = { name: float(price) for name, price in zip(unique_names, pricedata) }
print(prices['AA']*50)

current_value = 0.0
for holding in porfolio:
	current_value += holding['shares'] * prices[holding['name']]
print(current_value)

current_value = sum([holding['shares']*prices[holding['name']] for holding in porfolio])
print(current_value)

# Sorting
def holding_name(holding):
	return holding['name']
porfolio.sort(key=holding_name)
print(porfolio)

def holding_price(holding):
	return holding['price']
porfolio.sort(key=holding_price)
print(porfolio)

porfolio.sort(key=lambda holding: holding['name'])
a = lambda x: 10*x
print(a(10))
b = lambda x, y: x+y
print(b(2,3))

min(porfolio, key=lambda holding: holding['price'])
max(porfolio, key=lambda holding: holding['price'])

import itertools
for name, items in itertools.groupby(porfolio, key=lambda holding: holding['name']):
	print('NAME: ', name)
	for it in items:
		print(it)

by_name = { name: list(items) 
			for name, items in itertools.groupby(porfolio, key=lambda holding: holding['name']) }
print(by_name['IBM'])