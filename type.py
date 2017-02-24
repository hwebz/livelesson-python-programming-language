x = 42
y = 55.2
z = 'hello world'
class Point(object):
	pass
p = Point()
print(type(x), type(y), type(z), type(p)) # int, float, str, Point
print(type(str), type(object), type(int), type(float), type(Point)) # type

name = 'OtherPoint'
bases = (object, ) # 1-tuple
def __init__(self, x, y):
	self.x = x
	self.y = y

def move(self, dx, dy):
	self.x += dx
	delf.y += dy

methods = {
	'__init__': __init__,
	'move': move
}

OtherPoint = type(name, bases, methods)
p1 = OtherPoint(3,4)
print(p1.x,p1.y)

class mytype(type):
	def __new__(meta, clsname, bases, methods):
		print('Creating: ', clsname)
		print('Bases: ', bases)
		print('Methods: ', list(methods))
		return super().__new__(meta, clsname, bases, methods)

AnotherPoint = mytype(name, bases, methods)

class NewPoint(metaclass=mytype):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def move(self, dx, dy):
		self.x += dx
		self.y += dy
h = NewPoint(4, 5)
class D(NewPoint):
	def __init__(self, x, y):
		super().__init__(x, y)
	def york(self):
		pass
d = D(5, 6)