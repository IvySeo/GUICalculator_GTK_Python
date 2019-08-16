# author: Ivy Seo
# date: 08/15/2019
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

import calcul
import gi
import string
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#define
window = Gtk.Window()
textbox = Gtk.Entry()
table = Gtk.Table(4, 5, True)

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")

    def buttonClicked(self, widget):
        x = textbox.get_text() #get the input from textbox
        x = x + widget.num #helps displaying the input. w/o this, not work.
        textbox.set_text(x) #set the text

    def calculate(self, widget):
        x = textbox.get_text() #to get the input from text box
        x = str(calcul.calcu(x)) #fetch the number and send it to calculate
        textbox.set_text(x) #display the output 

# creates buttons 
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
btnMul = Gtk.Button(label='x')
btnDiv = Gtk.Button(label='/')
btnMod = Gtk.Button(label='%')
btnCal = Gtk.Button(label='=')

#define value of the button
btn1.num = '1' #value should be string, not int (bug) 
btn2.num = '2'
btn3.num = '3'
btn4.num = '4'
btn5.num = '5'
btn6.num = '6'
btn7.num = '7'
btn8.num = '8'
btn9.num = '9'
btn0.num = '0'

btnAdd.num = '+'
btnSub.num = '-'
btnMul.num = 'x'
btnDiv.num = '/'
btnMod.num = '%'
btnCal.num = '='

#activate the buttons when it's clicked.
Blist = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btnAdd, btnSub, btnMul, btnDiv, btnMod] #list for for-loop

w = MyWindow() 


for i in Blist:    #used for-loop for efficiency
    i.connect("clicked", w.buttonClicked) 

btnCal.connect("clicked", w.calculate) #activates calculate def


#locate
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
table.attach(btnMod, 3, 4, 2, 3)
table.attach(btnCal, 3, 4, 3, 5) #so the calculation button is bigger
table.attach(textbox, 0, 3, 0, 1)

window.add(table) #to add the table

window.show_all() #to display all the objects I created. w/o, can't see
window.connect("delete-event", Gtk.main_quit)  #exit
Gtk.main() #call the main()




