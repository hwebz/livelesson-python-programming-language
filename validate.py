class Typed(object):
	expected_type = object
	def __init__(self, name):
		self.name = name
	def __get___(self, instance, cls):
		return instance.__dict__[self.name]
	def __set__(self, instance, value):
		if not isinstance(value, self.expected_type):
			raise TypeError('Expected {}'.format(self.expected_type))
		instance.__dict__[self.name] = value
	def __getattr__(self, name):
		pass
	def __setattr__(self, name, value):
		if name not in ('name', 'date', 'shares', 'price'):
			raise AttributeError('No attribute {}'.format(name))
		super().__setattr__(name, value)
	def __delattr__(self, name):
		pass
class Integer(Typed):
	expected_type = int

class Float(Typed):
	expected_type = float

class String(Typed):
	expected_type = str

class ReadOnly(object):
	def __init__(self, obj):
		self._obj = obj
	def __getattr__(self, name):
		return getattr(self._obj, name)
	def __setattr__(self, name, value):
		if name == '_obj':
			super().__setattr__(name, value)
		else:
			raise AttributeError('Read only')

def typed(cls):
	for key, value in vars(cls).items():
		if isinstance(value, Typed):
			value.name = key
			cls._attributes.add(key)
	return cls

def structuretype(type):
	def __new__(meta, name, bases, methods):
		cls = super().__init__(name, bases, methods)
		cls = typed(cls) # Apply a class decorator
		return cls

def validate(**kwargs):
	def decorate(cls):
		for name, val in kwargs.items():
			setattr(cls, name, val(name))
		return cls
	return decorate

class Structure(metaclass=structuretype)
	def __setattr__(self, name, value):
		if name not in self._attributes:
			raise AttributeError('No attribute {}'.format(name))
		super().__setattr__(name, value)

# @typed # Using decorator for classes
@validate(name=String, shares=Integer, price=Float)
class Holding(Structure):
	# shares = Integer('shares')
	# price = Float('price')
	# name = String('name')
	# shares = Integer()
	# price = Float()
	# name = String()
	def __init__(self, name, date, shares, price):
		self.name = name
		self.date = date
		self.shares = shares
		self.price = price

	@property
	def cost(self):
		return self.shares * self.price

class Porfolio(object):
	# def append(self, item):
	# 	self.holdings.append(item)

	# def insert(self, index, item)
	# 	self.holdings.insert(index, item)

	# def sort(self, item):
	# 	self.holdings.sort()

	def __getattr__(self, name): # Can call all the methods of object
		return getattr(self.holdings, name)

# h.__getattribute__('name')
