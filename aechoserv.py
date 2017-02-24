# Aynchronous echo server

from socket import *
import asyncio

async def echo_server(address, loop):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(address)
	sock.listen(1)
	sock.setblocking(False)
	while True:
		# client, addr = sock.accept()
		client, addr = await loop.sock_accept(sock)
		print('Connection from', addr)
		# echo_handler(client)
		# t = threading.Thread(target=echo_handler, args=(client, loop))
		# t.start()
		loop.create_task(echo_handler(client, loop))

async def echo_handler(client, loop):
	while True:
		data = await loop.sock_recv(client, 10000)
		# client.recv(100000)
		if not data:
			break
		# client.sendall(b'Got: ' + data)
		await loop.sock_sendall(client, b'Got: ' + data)
	print('Connection closed')
	client.close()

# if __name__ == '__main__':
# 	# echo_server(('', 25000))
# 	loop = asyncio.get_event_loop()
# 	loop.run_until_complete(echo_server(('', 25000), loop))


import types
class Loop(object):
	@types.coroutine
	def sock_recv(self, sock, maxsize):
		result = yield ('recv', sock, maxsize)
		return result
	@types.coroutine
	def sock_sendall(self, sock, data):
		result = yield ('sendall', sock, data)
		return result
loop = Loop()
coro = echo_handler('somesocket', loop)
coro.send(None)
coro.send(b'Hello') # Run in python command