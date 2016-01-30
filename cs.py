"""Class scope demononstration module """
def mf():
	return "module function (can be used like a class in "\
			"other languages): mf()"

class SC:
	def __init__(self):
		self.siv =" superclass instance variable"
		self.__psiv = "private superclass instance variable"
	def sm(self):
		return "superclass method"
	def __spm(self):
		return " superclass private method"

class C(SC):
	def __init__(self):
		SC.__init__(self)
		self.__piv = "private instance variable: self.__piv"

