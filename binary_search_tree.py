"""
Code taken from gist.github.com/thinkphp/1450738
"""

class Node(object):
	"""
	Node used for binraty tree
	"""
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
		self.level = None # ???

class SearchTree(object):
	def __init__(self):
		self.root = None

	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			current = self.root
			while True:
				if val < current.val:
					if current.left:
						current = current.left
					else:
						current.left = Node(val)
						break;
				elif val >= current.val: # should not it be >=?
					if current.right:
						current = current.right
					else:
						current.right = Node(val)
						break
				else:
					break

	def inorder(self, node):
		if node is None:
			return None
		else:
			self.inorder(node.left)
			print node.val
			self.inorder(node.right)

	def preorder(self, node):
		if node is None:
			return None
		else:
			print node.val
			self.inorder(node.left)
			self.inorder(node.right)

	def postorder(self, node):
		if node is None:
			return None
		else:
			self.inorder(node.left)
			self.inorder(node.right)
			print node.val

