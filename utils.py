def factorial_generator():
	""" a simple function to compute factorial using generator"""
	count = 1
	fact = 1
	while True:
		yield fact
		count+=1
		fact = fact*count

def fibonacci_generator():
	""" a simple function to compute factorial using generator"""
	a, b = 0, 1

	while True:
		a, b = b, a+b
		yield a

def fibonacci_recursion(n):
	""" a simple function to compute factorial using generator"""
	if (n ==1 or n ==2):
		return 1
	return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def matrix_transpose_list_comprehension(mat):
	"""
	matrix transpose using list comprehension
	transpose a 4x3 matrix
	"""
	return [ [row[i] for row in mat] for i in range(3)]
 
def matrix_transpose_list_star(mat):
 	"""
 	matrix transpose using zip and multiple arguments
 	"""
 	return zip(*mat)

def flatten_nested_list_comprehension(li):
 	"""
 	flattens arbitrarily nested list
 	"""
 	return [x for y in li for x in y]

def flatten_nested_list_iter(li):
	"""
	flattens arbitrarily nested list using itertoold
	"""
	from itertools import chain
	return list(chain(*li))

def fizz_buzz(n):
	"""
	print fizz if divisible by 3, buzz if by 7 and 
	fizbuz if divisible by both
	"""
	if type(n) != int:
		raise ValueError('Not an integer')
	if n == 0:
		return None
	
	if not n%21:
		return 'fizzbuzz' 
	elif not n%3:
		return 'fizz'
	elif not n%7:
		return 'buzz'
	else:
		return n

def fizz_buzz_generator(n):
	"""
	print fizz if divisible by 3, buzz if by 7 and 
	fizbuz if divisible by both
	"""
	if type(n) != int:
		raise ValueError('Not an integer')
	'''
	if n == 0:
		return None
	'''
	if not x%21:
		yield 'fizzbuzz' 
	elif not x%3:
		yield 'fizz'
	elif not x%7:
		yield 'buzz'
	else:
		yield x

def use_enumerate(li=None):
	"""
	How is enumerate used
	"""
	if not li:
		li = ['spring', 'summer', 'fall', 'winter']
	return list(enumerate(li)) # list(enumerate(li, start=1)) if do not want 0 as start index

def max_len_string():
	"""
	determine the longest string in a list
	"""	
	list_string = ['determine', 'the', 'longest', 'string', 'in', 'a', 'list']
	max(li, lambda s: len(s))

def reduce_add_list_numbers(li):
	"""
	adds all numbers in a list
	"""
	return reduce(lambda x1, x2: x1	+x2, li)

def sum_list(li):
	'''
	Summing up a series using sum function
	'''
	return sum(li)

######## Example of sorting complex object ###################
class Student:
	def __init__(self, name, grade, age):
		self.name = name
		self.grade = grade
		self.age = age
	
	def __repr__(self):
		return repr((self.name, self.grade, self.age))
	

def sort_complex_object():
	"""
	example code that shows how to sort complex objects like
	dict etc using a key
	"""

	student_objects = [
		Student('john', 'A', 15),
		Student('jane', 'B', 12),
		Student('Nirmalya', 'A', 16)
	]
	return sorted(student_objects, key= lambda Student: Student.age)

######## Example of sorting complex object ###################