class Parent(object):
	def __init__(self, value):
		self.value = value

	def spam(self):
		print('Parent.spam', self.value)

	def grok(self):
		print('Parent.grok')
		self.spam()

class Child(Parent):
	def spam(self):
		print('Child.spam', self.value)

class Child2(Parent):
	def spam(self):
		print('Child2.spam', self.value)
		super().spam()

class Child3(Parent):
	def __init__(self, value, extra):
		self.extra = extra
		super().__init__(value) # Initialize parent

class Parent2(object):
	def yow(self):
		print('Parent2.yow')

class Child4(Parent, Parent2):
	pass

c = Child4(42)
print(c.spam())
print(c.grok())
print(c.yow())


class ParentClass(object):
	def __init(self):
		pass
	def spam(self):
		print('Parent.spam')
		
class A(ParentClass):
	def spam(self):
		print('A.spam')
		super().spam()

class B(A):
	def spam(self):
		print('B.spam')
		super().spam()

b = B()
b.spam()
# B.__mro__ # to see order of method calling

class C(ParentClass):
	def spam(self):
		print('C.spam')
		super().spam()

class D(ParentClass):
	def spam(self):
		print('D.spam')
		super().spam()

class E(A, C, D):
	pass
e = E()
e.spam()

class F(D, C, A):
	pass
f = F()
f.spam()