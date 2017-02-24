class Holding(object):
	def __init__(self, name, date, shares, price):
		self.name = name
		self.date = date
		self.shares = shares
		self.price = price
		self._value = 32 # Private

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, newprice):
		if not isinstance(newprice,float):
			raise TypeError('Expected float')
		if newprice < 0:
			raise ValueError('Must >= 0')
		self._price = newprice

	@property
	def shares(self):
		return self._shares

	@shares.setter
	def shares(self, newshares):
		if not isinstance(newshares, int):
			raise TypeError('Expected int')
		self._shares = newshares

	def __repr__(self):
		return 'Holding({!r},{!r},{!r},{!r})'.format(self.name, self.date, self.shares, self.price)
		# use to print direct object within console
		# porfolio
	def __str__(self):
		return '{} shares of {} at ${:0.2f}'.format(self.shares, self.name, self.price)
		# use to print to string when using print function
		# h = Holding('AA','2017-06-07',100,32.2)
		# print(h)
	# @property # can call func as property h.cost
	def cost(self):
		return self.shares * self.price

	def sell(self, nshares):
		self.shares -= nshares

	def _func(self):
		print('hello')

# h.__class__
# p = h.__class__.dict__['shares'] # object = h.shares
# hasattr(p, '__get__')
# hasattr(p, '__set__')

h = Holding('AA', '2007-06-07', 100, 32.2)
print(h.__dict__['shares'])
print(h.name, h.shares, h.price)
print(h.cost())
print(Holding.__dict__['cost'](h))
h.sell(25)
print(h.cost())
s = h.sell
s(10)
print('%10s %10d %10.2f' % (h.name, h.shares, h.cost()))
setattr(h, 'name', 'YHOO')
print(getattr(h, 'shares'))
import csv

def read_porfolio(filename):
	porfolio = []
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			h = Holding(row[0], row[1], int(row[2]), float(row[3]))
			porfolio.append(h)
	return porfolio


total = 0.0
porfolio = read_porfolio('porfolio2.csv')
for h in porfolio:
	total += h.shares * h.price
	# del h.date
print('Total cost: ', total)
names = [h.name for h in porfolio]
print(names)
# date = [h.date for h in porfolio]
# print(date)

import table
output_columns = ['name', 'shares', 'price']
formatter = table.TextTableFormatter(width=20)
# for colname in output_columns:
	# print(colname, '=', getattr(h, colname))
	# table.print_table(porfolio, output_columns)
table.print_table(porfolio, output_columns, formatter)
formatter.print_table(porfolio, output_columns)

printer = table.TablePrinter(formatter)
printer.print_table(porfolio, output_columns)

formatter = table.CSVTableFormatter()
table.print_table(porfolio, output_columns, formatter)

formatter = table.HTMLTableFormatter()
table.print_table(porfolio, output_columns, formatter)

formatter = table.QuoteTextTableFormatter()
table.print_table(porfolio, output_columns, formatter)

formatter = table.Formatter()
table.print_table(porfolio, output_columns, formatter)

formatter = table.AnotherFormatter()
table.print_table(porfolio, output_columns, formatter)

class Porfolio(object):
	def __init__(self):
		self.holdings = []

	@classmethod
	def from_csv(cls, filename):
		self = cls()
		with open(filename, 'r') as f:
			rows = csv.reader(f)
			headers = next(rows)
			for row in rows:
				h = Holding(row[0], row[1], int(row[2]), float(row[3]))
				self.holdings.append(h)
		return self
	def total_cost(self):
		return sum([h.shares * h.price for h in self.holdings])

	# def size(self):
	# 	return len(self.holdings)

	# def getHolding(self, n):
	# 	return self.holdings[n]
	def __len__(self): # For get length
		return len(self.holdings)
	def __getitem__(self): # For get item
		if isinstance(n, str):
			return [h for h in self.holdings if h.name == n]
		else:
			return self.holdings[n]
	def __iter__(self): # For for loop
		return self.holdings.__inter__()
