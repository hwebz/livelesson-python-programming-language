class Manager(object):
	def __enter__(self):
		print('Entering')
		return 'some value'

	def __exit__(self, ty, val, tb):
		print('Exiting')
		print(ty, val, tb)

m = Manager()
with m:
	print('Hello World')
	for i in range(3):
		print(i)

with m as val:
	print('val =', val)

with m:
	print('Hello World')
	int('n/a')