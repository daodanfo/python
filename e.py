#!/usr/bin/python3 
from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)
tarots=["huaying","weite","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute","toute"]
lb = Listbox(root, yscrollcommand=sb.set)

for i in tarots:
    lb.insert(END,i)

lb.pack(side=RIGHT,fill=BOTH)

sb.config(command=lb.yview)

mainloop()