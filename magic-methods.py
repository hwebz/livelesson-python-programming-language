x = 42
x + 10
x * 10
x.__add__(10)
x.__mul__(10)
names = ['IBM', 'YHOO', 'MSFT']
names.__getitem__(0)
names[1] = 'FB'
names.__setitem__(1, 'FB')

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		print('Add', other)

p = Point(2, 3)
p + 10
p + 'hello'
p + [1, 2, 3]
p + (4, 5)