def func(x, y, z):
	print(x, y, z)

func(1, 2, 3)
func(1, z=3, y=2)

def other_func(x, *args):
	print(x)
	print(args)

other_func(1)
other_func(1, 2, 3, 4, 5)

def other_one(*args, **kwargs):
	print(args)
	print(kwargs)

other_one()
other_one(1, 2, 3, 4)
other_one(1, 2, x=3, y=4)
other_one(1, xmin=10, xmax=20, color='red')

args = (1, 2)
kwargs = {'c': 3, 'd': 4}
other_one(*args, **kwargs)

def add(x, y):
	print(x + y)
	return x + y

def add_wrapper(*args, **kwargs):
	print('Wrapping!')
	return add(*args, **kwargs)
add_wrapper(2, 3)
add_wrapper(y = 3, x = 2)
