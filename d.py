#!/usr/bin/python3 

from tkinter import *
root = Tk()
root.geometry("600x450")
frame = Frame(root,relief=RAISED,bd=2)
frame.pack(fill=X)
text = Text(root)
text.pack(expand=True,fill=BOTH)
def call():
    text.delete(1.0,END)
    b="jfiejfkljhsi;aljgkl;ajskfd;jkgjksla0"
    text.insert(INSERT,b)
mb = Menubutton(frame,text="tarot")
mb.pack(side=LEFT)
edmenu = Menu(mb,tearoff=False)
filemenu=Menu(edmenu,tearoff=False)
filemenu.add_command(label="yr",command=call)
edmenu.add_cascade(label="花影",menu=filemenu)
mb.config(menu=edmenu)












mainloop()


