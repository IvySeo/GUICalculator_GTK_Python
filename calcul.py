"""
----- How it works -----
For more details, and how it's used, read the comments on each line

1) def calc() is called from gui.py
2) there is a class calculation() and 
       inputValue = calculation() 
       operator = calculation()
   so each of them has their own lists
3) inputValue.push(eval(num)) : the inputs will be appended to the list of inputValue.
   So, the inputValue list (self.items=[]) will be added with the inputs
   (operator input element will be saved in operator list)
4) define() : to sort the input values and calculate
4.1) sort and define the variables : first input number, operator, second input number
4.2) calculate two numbers and push the value
4.3) the calculated value will be added to the inputValue list at the last
5) return inputValue.pop(): it will return the calculated value using pop() 
   because the value is located at the last of the inputValue list
   
- pop() will delete the data/reset after use (the list will be empty)
"""

# class and def
class calculation:
	def __init__(self):
		self.items=[] # list
		
	def errorTest(self): # value error test
	    while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break

	def push(self, num):
		self.items.append(num)  # appends a num to the end of the self.items list

	def pop(self):
		return self.items.pop() 

inputValue = calculation() 
operator = calculation()
# These will have their own list

def define():
     # save the last input elememt of the list into a variable (x, y, z)
     # and pop that element out (remove) from the list 
	x = inputValue.pop()  # the second input number (= the last from the list of inputValue list)
	y = operator.pop()    # operator input (the last/only element of the list of operator list)
	z = inputValue.pop()  # the first input number

	if y=='x':            # if the operator element is equal to 'x',
                errorTest()   # run the value error test
		inputValue.push(add(x,z)) 
		# x,z will be calculated and pushed to push()
		# then the calculated value will be added to the inputValue list at the last of the list
		# so when'return inputValue.pop()' is called, the calculated value will be returned

	elif y=='/':
                errorTest()
		inputValue.push(z/x) #since z is the first input number, z comes first

	elif y=='+':
                errorTest()
		inputValue.push(x+z)

	elif y=='-':
                errorTest()
		inputValue.push(z-x)

	elif y=='^':
                errorTest()
		inputValue.push(z**x)

# gui.py calls this one 
def calc(expr):
	num="" 
		
        inputValue.push(eval(num))   #eval() method returns the result evaluated from the expression
        define()                     #call the define() to calculate
	
	return inputValue.pop() 
# returns the value to gui.py 
# value = the last element from the list, which is the calculated value
				
			

		
			
