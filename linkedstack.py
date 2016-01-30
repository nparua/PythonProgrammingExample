
class Empty(Exception):
	pass

class Node(object):
	"""Imlementation of node
	   By deault, instances of both old and new-style classes 
	   have a dictionary for attribute storage. This wastes 
	   space for objects having very few instance variables. 
	   The space consumption can become acute when creating 
	   large numbers of instances.

		The default can be overridden by defining __slots__ 
		in a new-style class definition. The __slots__ 
		declaration takes a sequence of instance variables 
		and reserves just enough space in each instance to 
		hold a value for each variable. Space is saved 
		because __dict__ is not created for each instance.
	"""
	__slots__  = '_element', '_next'
	def __init__(self, element, next = None):
		self._element = element
		self._next = next

	def __str__(self):
		return "node  object with element {0}".format(self._element)

class SinglyLinkedStack(object):
	"""Stack implementation using singly linked list"""
	def __init__(self):
		""" create empty stack"""
		self._head = None
		self._size = 0

	def __len__(self):
		"""Returns number of elements in the stack"""
		return self._size

	def is_empty(self):
		"""returns true is the stack is empty"""
		return self._size == 0

	def push(self, e):
		"""Adds elements to to top of the stack"""
		self._head = Node(e, self._head)
		self._size +=1

	def top(self):
		"""
		Return (but do not remove) the element at the
		top of the stack.
		Raise Empty exception if the stack is empty
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		return self._head._element

	def pop(self):
		"""
		Remove and return the element from the top of the stack (lie LIFO)
		"""
		if self.is_empty():
			raise Empty("Stack is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		return answer

class SinglyLinkedQueue(object):
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size ==0

	def first(self):
		if self.is_empty:
			raise Empty("queue is empty")
		return self._head._element

	def enqueue(self, e):
		"""
		Add an element at the back of the queue
		"""
		new_node = Node(e)
		if self.is_empty:
			self._head = new_node
		else:
			self._tail._next = new_node
		self._tail = new_node
		self._size += 1
	'''
	def dequeue(self):
		"""
		remove and return the first element of the queue
		"""
		if self.is_empty():
			raise Empty("queue is empty")
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
	'''


