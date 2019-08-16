# gui.py: for GUI using gtk
# calcul.py: for calculation

class Calculate:
    def __init__(self):
        self.items=[]
   
    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

inputValue = Calculate()
operator = Calculate()

def calcu():
    x = inputValue.pop()
    y = operator.pop()
    z = inputValue.pop()

    if y == '+':
        while True:
            try: 
                 x = float(x)
                 y = float(x)
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        inputValue.push(add(x,z))
        

    elif y == '-':
        while True:
            try: 
                 x = float(x)
                 y = float(x)
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        inputValue.push(subtract(x,z))

    elif y == '/':
        while True:
            try: 
                 x = float(x)
                 y = float(x)
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        inputValue.push(divide(x,z))

    elif y == 'x':
        while True:
            try: 
                 x = float(x)
                 y = float(x)
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        inputValue.push(multiply(x,z))

    if y == '%':
        while True:
            try: 
                 x = float(x)
                 y = float(x)
            except ValueError:
                print("Invalid input")
                continue
            else:
                break
        inputValue.push(modular(x,z))



    





