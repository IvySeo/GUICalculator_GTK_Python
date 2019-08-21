
class calculation:
	def __init__(self):
		self.items=[]

	def push(self,num):
		self.items.append(num)

	def pop(self):
		return self.items.pop()

inputValue = calculation()
operator = calculation()


def define():
	x=inputValue.pop()
	y=operator.pop()
	z=inputValue.pop()

	if y=='*':
            while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break
		inputValue.push(add(x,z))

	elif y=='/':
            while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break
		inputValue.push(z/x)

	elif y=='+':
            while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break
		inputValue.push(x+z)

	elif y=='-':
            while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break
		inputValue.push(z-x)

	elif y=='^':
            while True:
                try:
                except ValueError:
                    print("Invalid input")
                    continue
                else:
                    break
		inputValue.push(z**x)

def calc(expr):
	num=""
		
	if num:
		inputValue.push(eval(num))
		define()
	return inputValue.pop()

				
			

		
			
