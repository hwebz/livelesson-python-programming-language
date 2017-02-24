import csv

f = open('porfolio2.csv', 'r')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, str, int, float]
for func, val in zip(types, row):
	print(func, val)

converted = [ func(val) for func, val in zip(types, row) ]
print(converted)

print(dict(zip(headers, converted)))

porfolio = []

def read_csv(filename, types, *, errors='warn'):
	'''
	Read a CSV file with type conversion into a list of dicts
	'''

	if errors not in { 'warn', 'silent', 'raise' }:
		raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")

	records = []
	with open(filename, 'r') as f:
		rows = csv.reader(f)
		headers = next(rows)
		for rowno, row in enumerate(rows, start=1):
			try:
				row = [ func(val) for func, val in zip(types, row) ]
			except ValueError as err:
				if errors == 'warn':
					print('Row: ', rowno, 'Bad row: ', row)
					print('Row: ', rowno, 'Reason: ', err)
				elif errors == 'raise':
					raise
				else:
					pass
			record = {
				'name': row[0],
				'date': row[1],
				'shares': row[2],
				'price': row[3],
			}
			records.append(record)
	return records

porfolio = read_csv('porfolio2.csv', [str, str, int, float])
print(porfolio)