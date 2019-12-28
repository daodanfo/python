#!/usr/bin/python3 
from tkinter import *
root = Tk()
root.title("my label")
root.geometry("738x625")

frame=Frame(root,width=700,height=600)
frame.grid(sticky=W)
frame2=Frame(root,width=350,height=400)
frame2.grid(sticky=W)




def wt():
    def fool():
        r="jkafjie;ajfd;jskaf;jiew;jagk;dsiao;j\
fei;jieoaj ;f\
"
        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,r)
    
     
    def mag():
        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"sh it")
    def pre():

       text=Text(frame,width=350,height=40)
       text.grid(row=0,rowspan=25,column=2,sticky=N)
       text.insert(INSERT,"comm a")
    def em():

        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"daj  iia")
    def emp():

        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"ddgssfhfdhssshhhsdfhhrrh")
    card = [("the f",0,fool),("m",1,mag),("highp",2,pre),("empo",3,em),("emper",4,emp),("emper",5,emp),("emper",6,emp),("emper",7,emp),("emper",8,emp),("emper",9,emp),("emper",10,emp),("emper",11,emp),("emper",12,emp),("emper",13,emp),("emper",14,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",15,emp),("emper",16,emp),("emper",17,emp),("emper",18,emp),("emper",19,emp),("emper",20,emp)]
    for i,j,k in card:
        button =Button(frame,width=10,text=i,command=k)
        button.grid(row=j,column=0,sticky=W)


def hy():
    def fool():
        r="jkafjie;ajfd;jskaf;jiew;jagk;dsiao;j\
fei;jieoaj隔热管热水管热水管热死个人;f\
"
        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,r)
    
     
    def mag():
        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"sh供热隔热管摄入过热时it")
    def pre():

       text=Text(frame,width=350,height=40)
       text.grid(row=0,rowspan=25,column=2,sticky=N)
       text.insert(INSERT,"comm功夫大使馆热水供热公司热a")
    def em():

        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"daj更广泛的公司热热又有一天突然 iia")
    def emp():

        text=Text(frame,width=350,height=40)
        text.grid(row=0,rowspan=25,column=2,sticky=N)
        text.insert(INSERT,"符外回顾和素如顺利回归了和入市绿化管理人手里")
    card = [("the f",0,fool),("m",1,mag),("highp",2,pre),("empo",3,em),("emper",4,emp),("emper",5,emp),("emper",6,emp),("emper",7,emp),("emper",8,emp),("emper",9,emp),("emper",10,emp),("emper",11,emp),("emper",12,emp),("emper",13,emp),("emper",14,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",4,emp),("emper",15,emp),("emper",16,emp),("emper",17,emp),("emper",18,emp),("emper",19,emp),("emper",20,emp)]
    for i,j,k in card:
        button =Button(frame,width=10,text=i,command=k)
        button.grid(row=j,column=0,sticky=W)


 
menubar = Menu(root)
 
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='维特', command=wt)
filemenu.add_command(label='花影', command=hy)
menubar.add_cascade(label='Tarot', menu=filemenu)   #创建级联菜单，menu选项指定下一级的菜单是什么
 
 
editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='quit', command=root.quit)
menubar.add_cascade(label='退出', menu=editmenu) 
 
root.config(menu=menubar)



'''

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, str(i))

lb.pack(side=LEFT, fill=BOTH)

sb.config(command=button.yview)
'''


mainloop()
