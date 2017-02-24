f = open('porfolio.csv', 'r')
data = f.read()
print(data)
for line in f:
	print(line)
f.close()

with open('porfolio.csv', 'r') as f:
	f.read()

a = 'hello world'
b = "hello world"
c = '"IBM","2006-07-09","100","70.44"'
print(a[0])
print(a[-2])
print(a[0:5])
print(a[:5])
print(a[-5:])
print(len(b))
print(a + b)
a = a.strip() # strip spaces, new line characters
a.replace('ll', 'kk')
parts = c.split(',')
parts[0] = parts[0].strip('"')
parts[2] = parts[2].strip('"')
parts[3] = parts[3].strip('"')
parts[2] = int(parts[2])
parts[3] = float(parts[3])
print(parts[2] * parts[3])
