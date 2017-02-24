async def greeting(name):
	print('Hello ', name)
g = greeting('John Doe')

import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(g)

async def hello():
	names = ['Jack', 'John', 'Jimmy']
	for name in names:
		print(await greeting(name))

h = hello()
loop.run_until_complete(h)

async def fib(n):
	if n <= 2:
		return 1
	else:
		return await fib(n - 1) + await fib(n - 2)

f = fib(10)
print(loop.run_until_complete(f))