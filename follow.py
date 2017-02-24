# Watch a log file (stocks in this case)

import os
import time

def follow(filename):
	f = open(filename, 'r')
	f.seek(0, os.SEEK_END)

	while True:
		line = f.readline()
		if not line:
			time.sleep(0.1)
			continue 	# Retry
		yield line 		# Emit a line

# f = open('stocklog.csv')
# lines = f.readlines()

for line in follow('stocklog.csv'):
	row = line.split(',')
	change = float(row[3])
	if change < 0:
		name = row[0]
		price = row[1]
		print('{:>10s} {:>10s} {:>10.2f}: '.format(name, shares, price))

def grep(names, rows):
	for row in rows:
		if row[0] in names:
			yield row

matching = grep({'MSFT', 'IBM', 'CAT', 'AA'}, rows)
matching.__next__();

types = [str, float, str, str, float, float, float, float, int]
converted = ([func(val) for func, val in zip(types, row)] for row in matching)
converted.__next__()

negchange = (row for row in converted if row[4] < 0)
negchange.__next__()

import csv
def parse_stock_data(lines):
	rows = csv.reader(lines)
	types = [str, float, str, str, float, float, float, float, int]
	converted = ([func(val) for func, val in zip(types, rows)] for row in rows)
	return converted
