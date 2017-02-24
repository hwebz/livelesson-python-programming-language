import csv

total = 0.0

with open('porfolio.csv', 'r') as f:
#f = open('porfolio.py', 'r')
	headers = next(f)		# Skip a single input
	for line in f:
		line = line.strip() # Strip whitespace
		parts = line.split(',')
		parts[0] = parts[0].strip('"')
		parts[1] = parts[1].strip('"')
		parts[2] = int(parts[2])
		parts[3] = float(parts[3])
		print(parts)
		total += parts[2] * parts[3]

print ('Total cost: ', total)

# Using CSV library
total = 0.0
f = open('porfolio2.csv', 'r')
rows = csv.reader(f)
headers = next(rows)
for row in rows:
	row[2] = int(row[2])
	row[3] = float(row[3])
	print(row)
	total += row[2] * row[3]

print('Total cost: ', total)


# import portie.csvwriting as csvwriting
from . import csvwriting
# porfolio = csvwriting.read_csv('porfolio2.csv', [str, str, int, float], errors='silent')

def read_porfolio(filename, *, errors='warn'):
	return csvwriting.read_csv(filename, [str, str, int, float], errors=errors)

if __name__ == '__main__':
	porfolio = read_porfolio('porfolio2.csv')

	total = 0.0
	for holding in porfolio:
		total += holding['shares'] * holding['price']
	print('Total cost: ', total)