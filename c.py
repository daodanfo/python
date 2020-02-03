#!/usr/bin/python3 

from tkinter import *

def makeCascadeMenu():

     Cascade_button = Menubutton(mBar, text='Cascading Menus', underline=0)
     Cascade_button.pack(side=LEFT, padx="2m")
     Cascade_button.menu = Menu(Cascade_button)
 

     Cascade_button.menu.choices = Menu(Cascade_button.menu)

     Cascade_button.menu.choices.weirdones = Menu(Cascade_button.menu.choices)
 

     Cascade_button.menu.choices.weirdones.add_command(label='avacado', command=lambda:print('hello'))
     Cascade_button.menu.choices.weirdones.add_command(label='belgian endive')
     Cascade_button.menu.choices.weirdones.add_command(label='beefaroni')
 

     Cascade_button.menu.choices.add_command(label='Chocolate')
     Cascade_button.menu.choices.add_command(label='Vanilla')
     Cascade_button.menu.choices.add_command(label='TuttiFruiti')
     Cascade_button.menu.choices.add_command(label='WopBopaLoopBapABopBamBoom')
     Cascade_button.menu.choices.add_command(label='Rocky Road')
     Cascade_button.menu.choices.add_command(label='BubbleGum')
     Cascade_button.menu.choices.add_cascade(
         label='Weird Flavors',
         menu=Cascade_button.menu.choices.weirdones)
 
     
     Cascade_button.menu.add_cascade(label='more choices',
                                     menu=Cascade_button.menu.choices)
 
     Cascade_button['menu'] = Cascade_button.menu
 
     return Cascade_button

root = Tk()
root.geometry('600x300')

mBar = Frame(root, relief=RAISED, borderwidth=2)
mBar.pack(fill=X)
Cascade_button = makeCascadeMenu()
mBar.tk_menuBar(Cascade_button)

root.title('menu demo')
root.iconname('menu demo')
mainloop()