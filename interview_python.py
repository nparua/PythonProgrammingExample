"""
Q. Difference between sort and sorted

A. li.sort() sorts list in place, sort is a function of list
   sorted is a function, and it creates a new sorted list keeping 
   the original in pace. sorted can also be used on other iterables
"""

li = [5, 2, 4, 3, 1]
s = sorted(li)
print li
print s

student_tuple = [
('Ahona', 'A', 11),
('Soma', 'A', 47),
('Nirmalya', 'B', 45)
]

sorted(student_tuple, key=lambda student: student[2])
#sort using itemgetter and attrgetter module
from operator import itemgetter, attrgetter
sorted(student_tuple, key=itemgetter(2))

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

def sort_complex_object_attrgetter():
	from operator import itemgetter, attrgetter
	student_objects = [
		Student('john', 'A', 15),
		Student('jane', 'B', 12),
		Student('Nirmalya', 'A', 16)
	]
	return sorted(student_objects, key= attrgetter('age'))

def sort_count():
	# from the following list sort the list with increasing number of !
	from operator import methodcaller
	messages = ['critical!!!', 'hurry!', 'standby', 'immediate!!' ]
	return sorted(messages, key=methodcaller('count', '!'))

"""
Use operator module to elementwise multiplication of two lists
"""
from operator import mul
map(mul, [0,1,2,3], [3,4,5,6])

# get a jot product
sum(map(mul, [0,1,2,3], [3,4,5,6]))


"""
count list of lines from a file say binary_search_tree.py
"""
len_list = [ len(x) for x in open('binary_search_tree.py')] #using list comprehension
it = ( len(x) for x in open('binary_search_tree.py'))

#get list of file from a directory
def get_listof_file(**kwargs):
	'''
	usage:
	from interview_python import get_listof_file
	it = get_listof_file(dir='data')
	it.next()
	'''
	import glob
	import os
	dir = kwargs.get('dir')
	filepath = os.path.join(dir,'*')
	return glob.iglob(filepath)

