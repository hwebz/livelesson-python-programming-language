# def print_table(objects, colnames):
# 	'''
# 	Make a nicely formatted table showing attributes from a list of objects
# 	'''
# 	# Emit table headers
# 	for colname in colnames:
# 		print('{:>10s}'.format(colname), end=' ')
# 	print()
# 	for obj in objects:
# 		# Emit a row of table data
# 		for colname in colnames:
# 			print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
# 		print()
import sys
from abc import ABC, abstractmethod
def print_table(objects, colnames, formatter):
	'''
	Make a nicely formatted table showing attributes from a list of objects
	'''
	if not isinstance(formatter, TableFormatter):
		raise TypeError('formatter must be a TableFormatter')
	formatter.headings(colnames)
	for obj in objects:
		rowdata = [str(getattr(obj, colname)) for colname in colnames]
		formatter.row(rowdata)

class TablePrinter(object):
	def __init__(self, formatter):
		self.formatter = formatter
	def print_table(self, objects, colnames):
		self.formatter.headings(colnames)
		for obj in objects:
			rowdata = [str(getattr(obj, colname)) for colname in colnames]
			self.formatter.row(rowdata)

_formatters = {}
def register_formatter(name, cls):
	_formatters[name] = cls

class TableMeta(type):
	def __init__(cls, clsname, bases, methods):
		super().__init___(clsname, bases, methods)
		if hasattr(cls, 'name')
			_formatters[cls.name] = cls

class TableFormatter(metaclass=TableMeta):
	# Serves a design spec for making tables (use inheritance to customize)
	def __init__(self, outfile=None):
		if outfile == None:
			outfile = sys.stdout
		self.outfile = outfile
	def print_table(self, objects, colnames):
		self.headings(colnames)
		for obj in objects:
			rowdata = [str(getattr(obj, colname)) for colname in colnames]
			self.row(rowdata)
	@abstractmethod
	def headings(self, headers):
		# raise NotImplementedError # Must implemented
		pass
	@abstractmethod
	def row(self, rowdata):
		# raise NotImplementedError # Must implemented
		pass

class TextTableFormatter(TableFormatter):
	name = 'text'
	def __init__(self, outfile=None, width=10):
		super().__init__(outfile) # Initialize parent
		self.width = width
	def headings(self, headers):
		for header in headers:
			print('{:>{}s}'.format(header, self.width), end=' ', file=self.outfile)
		print(file=self.outfile)
	def row(self, rowdata):
		for item in rowdata:
			print('{:>{}s}'.format(item, self.width), end=' ', file=self.outfile)
		print(file=self.outfile)
# register_formatter('text', TextTableFormatter)

class CSVTableFormatter(TableFormatter):
	name = 'csv'
	def headings(self, headers):
		print(','.join(headers))
	def row(self, rowdata):
		print(','.join(rowdata))
# register_formatter('csv', CSVTableFormatter)

class HTMLTableFormatter(TableFormatter):
	name = 'html'
	def headings(self, headers):
		print('<tr>', end='')
		for h in headers:
			print('<th>{}</th>'.format(h), end='', file=self.outfile)
		print('</tr>')
	def row(self, rowdata):
		print('<tr>', end='')
		for r in rowdata:
			print('<td>{}</td>'.format(r), end='', file=self.outfile)
		print('</tr>')
# register_formatter('html', HTMLTableFormatter)

class QuoteTextTableFormatter(TextTableFormatter):
	def row(self, rowdata):
		# Put quotes around all values
		quoted = ['"{}"'.format(d) for d in rowdata ]
		super().row(quoted)

class QuotedMixin(object):
	def row(self, rowdata):
		quoted = ['"{}"'.format(d) for d in rowdata]
		super().row(quoted)

class Formatter(QuotedMixin, CSVTableFormatter):
	pass

class AnotherFormatter(QuotedMixin, HTMLTableFormatter):
	pass

# _formatters = {
# 	'text': TextTableFormatter,
# 	'csv': CSVTableFormatter,
# 	'html': HTMLTableFormatter
# }

def create_formatter(name):
	# if name == 'text':
	# 	formatter = TextTableFormatter
	# elif name == 'csv':
	# 	formatter = CSVTableFormatter
	# elif name = 'html':
	# 	formatter = HTMLTableFormatter
	# else:
	# 	raise ValueError('Unknown format {}'.format(name))
	# return formatter
	formatter = _formatters.get(name)
	if not formatter:
		raise ValueError('Unknown format {}'.format(name))
	return formatter()

formatter = create_formatter('html')
formatter.print_table('porfolio2.csv', ['name', 'shares', 'price'])