def another_function(func):
	def other_func():
		val = "the results of %s is %s " % (func(),
												 eval(func())
												 )
		return val
	return other_func

@another_function 
"""symbol followed by the name of
the function that we will be using to “decorate” our regular with. To apply the decorator, you
just put it on the line before the function definition. Now when we call **a_function
"""
def a_function():
	return "1 + 1"


if __name__ == "__main__":
	value = a_function()
	print(value)
	#decorator = another_function(a_function)
	#print(decorator())