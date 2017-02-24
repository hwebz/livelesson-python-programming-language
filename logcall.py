from functools import wraps
def logged(func):
	# Idea: Give me a function, I'll put logging
	# around it

	print('Adding logging to ', func.__name__)

	@wraps(func)
	def wrapper(*args, **kwargs):
		print('Calling {}'.format(func.__name__))
		return func(*args, **kwargs)
	# wrapper.__name__ = func.__name__
	# wrapper.___doc__ = func.__doc__
	return wrapper

def logformat(fmt): 
	def logged(func):
		# Idea: Give me a function, I'll put logging
		# around it

		print('Adding logging to ', func.__name__)

		@wraps(func)
		def wrapper(*args, **kwargs):
			print(fmt.format(func=func))
			return func(*args, **kwargs)
		# wrapper.__name__ = func.__name__
		# wrapper.___doc__ = func.__doc__
		return wrapper
	return logged

decorate = logformat('CALLING {func.__name__}')
@decorate # Using decorator instead
def add(x, y):
	'''
	Add x and y
	'''
	# print('Calling add') // Add log manually
	return x + y
# add = logged(add) // Using logged function

# @logged
@decorate
def sub(x, y):
	# print('Calling sub')
	return x - y
# sub = logged(sub)

@decorate
def mul(x, y):
	# print('Calling mul')
	return x * y
# mul = logged(mul)

# sub = decorate(sub)

def logmethods(cls):
	for key, value in list(vars(cls).items()):
		if callable(value):
			# Is it a method? If so, decorate
			setattr(cls, key, decorate(value))
	return cls
	
@logmethods
class Animals(object):
	def __init__(self, name):
		self.name = name
	def bake(type):
		print("Baking ", type)