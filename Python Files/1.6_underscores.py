class Test(object):
	def __init__(self):
		self.__name = 'Bob'
		self._day = 'Tuesday'

t = Test()
print(t._day)                   # Output: Tuesday
print(t.__name)                 # Output: AttributeError: 'Test' object has no attribute '__name'
print(t._Test__name)            # Output: Bob