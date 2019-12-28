#!/usr/bin/python3 
import a
from tkinter import *
root = Tk()
root.geometry("700x650")
frame = Frame(root,relief=RAISED,bd=2)
frame.pack(fill=X)
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)
text = Text(root,yscrollcommand=sb.set,font=65)
text.pack(expand=True,fill=BOTH)
class YR:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yr_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yr_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yr_kh)

class MSS:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.mss_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.mss_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.mss_kh)
class NJS:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.njs_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.njs_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.njs_kh)
class NH:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.nh_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.nh_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.nh_kh)
    
class HD:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.hd_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.hd_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.hd_kh)

class JH:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jh_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jh_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jh_kh)


class LR:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.lr_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.lr_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.lr_kh)
        

class ZC:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zc_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zc_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zc_kh)

class LL:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ll_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ll_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ll_kh)

class YS:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ys_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ys_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ys_kh)

class MY:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.my_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.my_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.my_kh)

class ZY:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zy_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zy_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.zy_kh)
class DD:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.dd_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.dd_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.dd_kh)

class SS:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ss_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ss_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ss_kh)

class JZ:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jz_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jz_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.jz_kh)
class EM:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.em_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.em_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.em_kh)

class T:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.t_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.t_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.t_kh)


class XX:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.xx_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.xx_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.xx_kh)


class YL:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yl_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yl_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.yl_kh)

class TY:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ty_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ty_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.ty_kh)


class SP:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sp_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sp_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sp_kh)


class SJ:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sj_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sj_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sj_kh)

class Q1:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz1_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz1_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz1_kh)
        
class Q2:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz2_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz2_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz2_kh)

class Q3:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz3_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz3_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz3_kh)
class Q4:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz4_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz4_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz4_kh)

class Q5:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz5_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz5_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz5_kh)
class Q6:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz6_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz6_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz6_kh)
class Q7:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz7_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz7_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz7_kh)
class Q8:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz8_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz8_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz8_kh)
class Q9:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz9_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz9_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz9_kh)
class Q10:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz10_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz10_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz10_kh)
class Q11:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz11_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz11_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz11_kh)
class Q12:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz12_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz12_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz12_kh)
class Q13:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz13_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz13_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz13_kh)
class Q14:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz14_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz14_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qz14_kh)
class S1:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb1_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb1_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb1_kh)
        
class S2:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb2_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb2_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb2_kh)            

class S3:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb3_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb3_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb3_kh)

class S4:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb4_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb4_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb4_kh)

class S5:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb5_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb5_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb5_kh)
class S6:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb6_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb6_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb6_kh)
class S7:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb7_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb7_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb7_kh)

class S8:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb8_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb8_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb8_kh)
class S9:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb9_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb9_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb9_kh)

class S10:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb10_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb10_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb10_kh)

class S11:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb11_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb11_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb11_kh)
class S12:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb12_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb12_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb12_kh)
class S13:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb13_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb13_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb13_kh)
class S14:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb14_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb14_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.sb14_kh)

class B1:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj1_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj1_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj1_kh)



class B2:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj2_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj2_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj2_kh)

class B3:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj3_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj3_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj3_kh)

class B4:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj4_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj4_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj4_kh)

class B5:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj5_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj5_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj5_kh)

class B6:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj6_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj6_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj6_kh)

class B7:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj7_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj7_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj7_kh)

class B8:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj8_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj8_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj8_kh)


class B9:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj9_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj9_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj9_kh)

class B10:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj10_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj10_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj10_kh)



class B11:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj11_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj11_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj11_kh)


class B12:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj12_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj12_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj12_kh)


class B13:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj13_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj13_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj13_kh)


class B14:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj14_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj14_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.bj14_kh)

class QB1:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb1_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb1_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb1_kh)


class QB2:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb2_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb2_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb2_kh)

class QB3:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb3_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb3_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb3_kh)


class QB4:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb4_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb4_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb4_kh)


class QB5:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb5_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb5_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb5_kh)


class QB6:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb6_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb6_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb6_kh)


class QB7:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb7_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb7_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb7_kh)


class QB8:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb8_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb8_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb8_kh)

class QB9:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb9_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb9_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb9_kh)

class QB10:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb10_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb10_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb10_kh)

class QB11:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb11_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb11_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb11_kh)

class QB12:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb12_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb12_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb12_kh)

class QB13:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb13_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb13_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb13_kh)

class QB14:
    def ast(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb14_ast)
    def qs(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb14_qs)
    def kh(self):
        text.delete(1.0,END)
        text.insert(INSERT,a.qb14_kh)


























        
     

yr=YR()
mss=MSS()
njs=NJS()
nh=NH()
hd=HD()
jh=JH()
lr=LR()
zc=ZC()
ll=LL()
ys=YS()
my=MY()
zy=ZY()
dd=DD()
ss=SS()
jz=JZ()
em=EM()
t=T()
xx=XX()
yl=YL()
ty=TY()
sp=SP()
sj=SJ()
q1=Q1()
q2=Q2()
q3=Q3()
q4=Q4()
q5=Q5()
q6=Q6()
q7=Q7()
q8=Q8()
q9=Q9()
q10=Q10()
q11=Q11()
q12=Q12()
q13=Q13()
q13=Q13()
q14=Q14()
s1=S1()
s2=S2()
s3=S3()
s4=S4()
s5=S5()
s6=S6()
s7=S7()
s8=S8()
s9=S9()
s10=S10()
s11=S11()
s12=S12()
s13=S13()
s14=S14()
b1=B1()
b2=B2()
b3=B3()
b4=B4()
b5=B5()
b6=B6()
b7=B7()
b8=B8()
b9=B9()
b10=B10()
b11=B11()
b12=B12()
b13=B13()
b14=B14()
qb1=QB1()
qb2=QB2()
qb3=QB3()
qb4=QB4()
qb5=QB5()
qb6=QB6()
qb7=QB7()
qb8=QB8()
qb9=QB9()
qb10=QB10()
qb11=QB11()
qb12=QB12()
qb13=QB13()
qb14=QB14()

mb = Menubutton(frame,text="爱上塔罗牌",relief=RAISED)
mb.pack(side=LEFT)
mbmenu = Menu(mb,tearoff=False)
amenu=Menu(mbmenu,tearoff=False)
bmenu=Menu(mbmenu,tearoff=False)
cmenu=Menu(bmenu,tearoff=False)
dmenu=Menu(bmenu,tearoff=False)
emenu=Menu(bmenu,tearoff=False)
mbmenu.add_cascade(label="大阿卡那",menu=amenu)
mbmenu.add_cascade(label="权杖",menu=bmenu)
mbmenu.add_cascade(label="圣杯",menu=cmenu)
mbmenu.add_cascade(label="宝剑",menu=dmenu)
mbmenu.add_cascade(label="钱币",menu=emenu)

card=[("愚人",yr.ast),("魔术师",mss.ast),("女祭司",njs.ast),("女皇",nh.ast),("皇帝",hd.ast),("教宗/教皇",jh.ast),("恋人",lr.ast),("战车",zc.ast),("隐士",ys.ast),("命运之轮",my.ast)\
,("正义",zy.ast),("倒吊者",dd.ast),("死神",ss.ast),("节制",jz.ast),("恶魔",em.ast),("塔",t.ast),("星星",xx.ast),("月亮",yl.ast),("太阳",ty.ast),("审判",sp.ast),("世界",sj.ast)]
for i,k in card:

    amenu.add_command(label=i,command=k)

qcard=[("权杖1",q1.ast),("权杖2",q2.ast),("权杖3",q3.ast),("权杖4",q4.ast),("权杖5",q5.ast),("权杖6",q6.ast),("权杖7",q7.ast),("权杖8",q8.ast),("权杖9",q9.ast),\
("权杖10",q10.ast),("权杖侍从",q11.ast),("权杖骑士",q12.ast),("权杖王后",q13.ast),("权杖国王",q14.ast)]
scard=[("圣杯1",s1.ast),("圣杯2",s2.ast),("圣杯3",s3.ast),("圣杯4",s4.ast),("圣杯5",s5.ast),("圣杯6",s6.ast),("圣杯7",s7.ast),("圣杯8",s8.ast),("圣杯9",s9.ast),\
("圣杯10",s10.ast),("圣杯侍从",s11.ast),("圣杯骑士",s12.ast),("圣杯王后",s13.ast),("圣杯国王",s14.ast)]
bcard=[("宝剑1",b1.ast),("宝剑2",b2.ast),("宝剑3",b3.ast),("宝剑4",b4.ast),("宝剑5",b5.ast),("宝剑6",b6.ast),("宝剑7",b7.ast),("宝剑8",b8.ast),("宝剑9",b9.ast),\
("宝剑10",b10.ast),("宝剑侍从",b11.ast),("宝剑骑士",b12.ast),("宝剑王后",b13.ast),("宝剑国王",b14.ast)]
qbcard=[("钱币1",qb1.ast),("钱币2",qb2.ast),("钱币3",qb3.ast),("钱币4",qb4.ast),("钱币5",qb5.ast),("钱币6",qb6.ast),("钱币7",qb7.ast),("钱币8",qb8.ast),\
("钱币9",qb9.ast),("钱币10",qb10.ast),("钱币侍从",qb11.ast),("钱币骑士",qb12.ast),("钱币王后",qb13.ast),("钱币国王",qb14.ast)]

for i,k in qcard:
    bmenu.add_command(label=i,command=k)

for i,k in scard:
    cmenu.add_command(label=i,command=k)
    
for i,k in bcard:
    dmenu.add_command(label=i,command=k)

for i,k in qbcard:
    emenu.add_command(label=i,command=k)





mb.config(menu=mbmenu)

















mb1 = Menubutton(frame,text="其实你已经很塔罗了",relief=RAISED)
mb1.pack(side=LEFT)
mb1menu = Menu(mb1,tearoff=False)
a1menu=Menu(mb1menu,tearoff=False)
b1menu=Menu(mb1menu,tearoff=False)
c1menu=Menu(b1menu,tearoff=False)
d1menu=Menu(b1menu,tearoff=False)
e1menu=Menu(b1menu,tearoff=False)
mb1menu.add_cascade(label="大阿卡那",menu=a1menu)
mb1menu.add_cascade(label="权杖",menu=b1menu)
mb1menu.add_cascade(label="圣杯",menu=c1menu)
mb1menu.add_cascade(label="宝剑",menu=d1menu)
mb1menu.add_cascade(label="钱币",menu=e1menu)
cards=[("愚人",yr.qs),("魔术师",mss.qs),("女祭司",njs.qs),("女皇",njs.qs),("皇帝",hd.qs),("教宗/教皇",jh.qs),("恋人",lr.qs),("战车",zc.qs),("隐士",ys.qs),\
        ("命运之轮",my.qs),("正义",zy.qs),("倒吊者",dd.qs),("死神",ss.qs),("节制",jz.qs),("恶魔",em.qs),("塔",t.qs),("星星",xx.qs),("月亮",yl.qs),("太阳",ty.qs),\
        ("审判",sp.qs),("世界",sj.qs)]

q1card=[("权杖1",q1.qs),("权杖2",q2.qs),("权杖3",q3.qs),("权杖4",q4.qs),("权杖5",q5.qs),("权杖6",q6.qs),("权杖7",q7.qs),("权杖8",q8.qs),("权杖9",q9.qs),\
("权杖10",q10.qs),("权杖侍从",q11.qs),("权杖骑士",q12.qs),("权杖王后",q13.qs),("权杖国王",q14.qs)]
s1card=[("圣杯1",s1.qs),("圣杯2",s2.qs),("圣杯3",s3.qs),("圣杯4",s4.qs),("圣杯5",s5.qs),("圣杯6",s6.qs),("圣杯7",s7.qs),("圣杯8",s8.qs),("圣杯9",s9.qs),\
("圣杯10",s10.qs),("圣杯侍从",s11.qs),("圣杯骑士",s12.qs),("圣杯王后",s13.qs),("圣杯国王",s14.qs)]
b1card=[("宝剑1",b1.qs),("宝剑2",b2.qs),("宝剑3",b3.qs),("宝剑4",b4.qs),("宝剑5",b5.qs),("宝剑6",b6.qs),("宝剑7",b7.qs),("宝剑8",b8.qs),("宝剑9",b9.qs),\
("宝剑10",b10.qs),("宝剑侍从",b11.qs),("宝剑骑士",b12.qs),("宝剑王后",b13.qs),("宝剑国王",b14.qs)]
q1bcard=[("钱币1",qb1.qs),("钱币2",qb2.qs),("钱币3",qb3.qs),("钱币4",qb4.qs),("钱币5",qb5.qs),("钱币6",qb6.qs),("钱币7",qb7.qs),("钱币8",qb8.qs),\
("钱币9",qb9.qs),("钱币10",qb10.qs),("钱币侍从",qb11.qs),("钱币骑士",qb12.qs),("钱币王后",qb13.qs),("钱币国王",qb14.qs)]

for i,k in cards:

    a1menu.add_command(label=i,command=k)


for i,k in q1card:
    b1menu.add_command(label=i,command=k)

for i,k in s1card:
    c1menu.add_command(label=i,command=k)
    
for i,k in b1card:
    d1menu.add_command(label=i,command=k)

for i,k in q1bcard:
    e1menu.add_command(label=i,command=k)

mb1.config(menu=mb1menu)


















mb2 = Menubutton(frame,text="塔罗葵花宝典",relief=RAISED)
mb2.pack(side=LEFT)
mb2menu = Menu(mb2,tearoff=False)
a2menu=Menu(mb2menu,tearoff=False)
b2menu=Menu(mb2menu,tearoff=False)
c2menu=Menu(b2menu,tearoff=False)
d2menu=Menu(b2menu,tearoff=False)
e2menu=Menu(b2menu,tearoff=False)
mb2menu.add_cascade(label="大阿卡那",menu=a2menu)
mb2menu.add_cascade(label="权杖",menu=b2menu)
mb2menu.add_cascade(label="圣杯",menu=c2menu)
mb2menu.add_cascade(label="宝剑",menu=d2menu)
mb2menu.add_cascade(label="钱币",menu=e2menu)
cardss=[("愚人",yr.kh),("魔术师",mss.kh),("女祭司",njs.kh),("女皇",nh.kh),("皇帝",hd.kh),("教宗/教皇",jh.kh),("恋人",lr.kh),("战车",zc.kh),("隐士",ys.kh),\
        ("命运之轮",my.kh),("正义",zy.kh),("倒吊者",dd.kh),("死神",ss.kh),("节制",jz.kh),("恶魔",em.kh),("塔",t.kh),("星星",xx.kh),("月亮",yl.kh),("太阳",ty.kh),\
        ("审判",sp.kh),("世界",sj.kh)]
q2card=[("权杖1",q1.kh),("权杖2",q2.kh),("权杖3",q3.kh),("权杖4",q4.kh),("权杖5",q5.kh),("权杖6",q6.kh),("权杖7",q7.kh),("权杖8",q8.kh),("权杖9",q9.kh),\
("权杖10",q10.kh),("权杖侍从",q11.kh),("权杖骑士",q12.kh),("权杖王后",q13.kh),("权杖国王",q14.kh)]
s2card=[("圣杯1",s1.kh),("圣杯2",s2.kh),("圣杯3",s3.kh),("圣杯4",s4.kh),("圣杯5",s5.kh),("圣杯6",s6.kh),("圣杯7",s7.kh),("圣杯8",s8.kh),("圣杯9",s9.kh),\
("圣杯10",s10.kh),("圣杯侍从",s11.kh),("圣杯骑士",s12.kh),("圣杯王后",s13.kh),("圣杯国王",s14.kh)]
b2card=[("宝剑1",b1.kh),("宝剑2",b2.kh),("宝剑3",b3.kh),("宝剑4",b4.kh),("宝剑5",b5.kh),("宝剑6",b6.kh),("宝剑7",b7.kh),("宝剑8",b8.kh),("宝剑9",b9.kh),\
("宝剑10",b10.kh),("宝剑侍从",b11.kh),("宝剑骑士",b12.kh),("宝剑王后",b13.kh),("宝剑国王",b14.kh)]
q2bcard=[("钱币1",qb1.kh),("钱币2",qb2.kh),("钱币3",qb3.kh),("钱币4",qb4.kh),("钱币5",qb5.kh),("钱币6",qb6.kh),("钱币7",qb7.kh),("钱币8",qb8.kh),\
("钱币9",qb9.kh),("钱币10",qb10.kh),("钱币侍从",qb11.kh),("钱币骑士",qb12.kh),("钱币王后",qb13.kh),("钱币国王",qb14.kh)]



for i,k in cardss:

    a2menu.add_command(label=i,command=k)

for i,k in q2card:
    b2menu.add_command(label=i,command=k)

for i,k in s2card:
    c2menu.add_command(label=i,command=k)
    
for i,k in b2card:
    d2menu.add_command(label=i,command=k)

for i,k in q2bcard:
    e2menu.add_command(label=i,command=k)
mb2.config(menu=mb2menu)








































mb3 = Menubutton(frame,text="退出",relief=RAISED)
mb3.pack(side=LEFT)
mb3menu = Menu(mb3,tearoff=False)
a3menu=Menu(mb3menu,tearoff=False)
a3menu.add_command(label="退出",command=root.quit)
mb3menu.add_cascade(label="退出",menu=a3menu)
mb3.config(menu=mb3menu)
mainloop()


