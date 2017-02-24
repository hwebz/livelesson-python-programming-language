#Tuples, Lists, Sets, Dicts
t = ('AA', '2011-06-07', 100, 32.2) # Tuples
len(t)
t[0]
name, date, shares, price = t
# t[2] = 50 # Cannot assign value
names = ['IBM', 'YHOO', 'AA', 'CAT']
names.append('IBM')
names.insert(1, 'FB')
names[2] = 'HPE'
nums = [45, 13, 20, 17]
distinct_names = { 'YHOO', 'IBM', 'MSFT', 'YHOO', 'AA', 'IBM'} # remove duplicated items
set(names)
'AA' in distinct_names
prices = {
	'IBM': 91.2,
	'MSFT': 45.23,
	'AA': 55.3,
	'YHOO': 67.7
}
prices['IBM']
'IBM'in prices
items = [ ('AA', 100, 32.2), ('MSFT', 50, 91.2) ]
prices = {
	'IBM': {
		'current': 91.2,
		'high': 95.5,
		'low': 45.5
	}
}

import portie.port as port
print(port.read_porfolio('porfolio2.csv'))

import portie
print(portie.read_csv('porfolio2.csv', [str, str, int, float]))