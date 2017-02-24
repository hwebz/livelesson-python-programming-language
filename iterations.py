names = ['YHOO', 'IBM', 'APPL']
for name in names:
	print(name)

it = names.__iter__()
it.__next__()
it.__next__()

f = open('porfolio2.csv', 'r')
it = f.__iter__()
it.__next__()

def countdown(n):
	print('Counting from ', n)
	while n > 0:
		yield n # Emit a value
		n -= 1
	print('Done')

for x in countdown(5):
	print(x)

c = countdown(5)
it = c.__iter__()
it.__next__()
it.__next__()

def grep(pattern, filename):
	with open(filename) as f:
		for line in f:
			if pattern in line:
				yield line

for line in grep('IBM', 'porfolio2.csv'):
	print(line)

nums = [1, 2, 3, 4, 5, 6]
squares = (x*x for x in nums)
print(squares)

for x in squares:
	print(x)

squares = [x*x for x in nums]
print(squares)
print(sum(squares))
print(sum((x*x for x in nums)))
print(sum(x*x for x in nums))

f = open('porfolio2.csv')
ibm = (line for line in f if 'IBM' in line)
for line in ibm:
	print(line)

class CountDown(object):
	def __init__(self, start):
		self.start = start
	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -= 1

c = CountDown(5)
for x in c:
	print(x)