class Date(object):
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
	@classmethod
	def from_string(cls, s):
		parts = s.split('-')
		return cls(int(parts[0]), int(parts[1]), int(parts[2]))

	@classmethod
	def today(cls):
		import time
		t =time.localtime()
		return cls(t.tm_year, t.tm_mon, t.tm_mday)

d = Date.from_string('2007-06-11')
print(d.year, d.month, d.day)
d = Date(2012, 5, 22)
print(d.year, d.month, d.day)
d = Date.today()
print(d.year, d.month, d.day)