# author: Ivy Seo
# date: 08/21/2019
# contact: ivy.rice.seo@gmail.com
# language: Python
# title: Calculator using gtk

# ------------- instruction -------------
# 1. pre-req: install python gtk command:
#   'sudo apt install python3-gi-cairo gir1.2-gtk-3.0'
# 2. 'python3 filename.py' to start the program
#-----------------------------------------

# gui.py: for GUI using gtk
# calcul.py: for calculation

#import calcul file to calculate and gtk files
import calcul 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#define
window = Gtk.Window()
table = Gtk.Table(4,5,True) #table size. 
textbox = Gtk.Entry()

#class and def
class MyWindow:
	def __init__(self):
		pass
	
        # when a button is clicked
	def buttonClicked(self,widget):
		x = textbox.get_text()
		x = x + widget.val        # displays the input
		textbox.set_text(x)        
		
	# when calculate (=) button is clicked	
	def calculate(self,widget):
		x = textbox.get_text()    # get text from textbox
		x = str(calcul.calc(x))   # send it to calcFile to calculate
		textbox.set_text(x)       # display the calculated in the textbox
	

w = MyWindow()

# creates buttons and label them
btn1 = Gtk.Button(label='1')
btn2 = Gtk.Button(label='2')
btn3 = Gtk.Button(label='3')
btn4 = Gtk.Button(label='4')
btn5 = Gtk.Button(label='5')
btn6 = Gtk.Button(label='6')
btn7 = Gtk.Button(label='7')
btn8 = Gtk.Button(label='8')
btn9 = Gtk.Button(label='9')
btn0 = Gtk.Button(label='0')

btnAdd = Gtk.Button(label='+')
btnSub = Gtk.Button(label='-')
btnMul = Gtk.Button(label='X')
btnDiv = Gtk.Button(label='/')
btnExp = Gtk.Button(label='^')
btnCal = Gtk.Button(label='=')

# define value of the button
# value should be string, not int (bug) 
buttons = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9] 

for i in range(len(buttons)):   # creates a range corresponding to the indexes in the list (0 to len(buttons) - 1)
	buttons[i].val=str(i)   # set their values using for-loop for shorter/simple code

btnAdd.val = '+'
btnSub.val = '-'
btnMul.val = 'x'
btnDiv.val = '/'
btnMod.val = '^'
btnCal.val = '='


# to activate button clicks
blists = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btnAdd, btnSub, btnMul, btnDiv, btnExp, btnCal]

for i in blists:
	i.connect("clicked",w.buttonClicked)
	
# the calculation button activation
btnCal.connect("clicked",w.calculate)

#locate the button location. check the image on 'ReadMe' on github
table.attach(btn1, 0, 1, 1, 2)
table.attach(btn2, 1, 2, 1, 2)
table.attach(btn3, 2, 3, 1, 2)
table.attach(btn4, 0, 1, 2, 3)
table.attach(btn5, 1, 2, 2, 3)
table.attach(btn6, 2, 3, 2, 3)
table.attach(btn7, 0, 1, 3, 4)
table.attach(btn8, 1, 2, 3, 4)
table.attach(btn9, 2, 3, 3, 4)
table.attach(btn0, 1, 2, 4, 5)
table.attach(btnAdd, 0, 1, 4, 5)
table.attach(btnSub, 2, 3, 4, 5)
table.attach(btnMul, 3, 4, 0, 1)
table.attach(btnDiv, 3, 4, 1, 2)
table.attach(btnExp, 3, 4, 2, 3)
table.attach(btnCal, 3, 4, 3, 5) 
table.attach(textbox, 0, 3, 0, 1)


window.add(table)
window.show_all()                                #to display all the objects I created.
window.connect("delete-event",Gtk.main_quit)     #exit
Gtk.main()
