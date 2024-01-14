from tkinter import *

def numclick(number):
    present_input=input.get()
    input.delete(0, END)
    input.insert(0, str(present_input) + str(number))
    
def clrclick():
    input.delete(0, END)
    
def addclick():
    global math
    math="add"
    present_input=input.get()
    global addnum
    addnum=float(present_input)
    input.delete(0, END)

def subclick():
    global math
    math="sub"
    present_input=input.get()
    global subnum
    subnum=float(present_input)
    input.delete(0, END)

def mulclick():
    global math 
    math="mul"
    present_input=input.get()
    global mulnum
    mulnum=float(present_input)
    input.delete(0, END)

def divclick():
    global math
    math="div"
    present_input=input.get()
    global divnum
    divnum=float(present_input)
    input.delete(0, END)

def sqrclick():
    global math
    math="sqr"
    present_input=input.get()
    global sqrnum
    sqrnum=float(present_input)
    
def eqlclick():
    second_num=int(input.get())
    input.delete(0, END)
    if math=="add":
        input.insert(0,addnum+second_num)
    elif math=="sub":
        input.insert(0,subnum-second_num)
    elif math=="mul":
        input.insert(0,mulnum*second_num)
    elif math=="div":
        input.insert(0,divnum/second_num)
    elif math=="sqr":
        input.insert(0,sqrnum**0.5)
        
def deciclick(point):
    current=input.get()
    input.delete(0,END)
    input.insert(0,str(current)+ str(point))
    
main=Tk()
main.title("Calculator")
main.geometry("340x365")
main.resizable(0,0)
main.configure(bg="#171010")

input=Entry(main, font=("arial 18 bold"), width=24, bd=5, justify=RIGHT, bg="#06113C", fg="white", insertbackground="red")
input.grid(row=0,column=0,columnspan=7,padx=10,pady=10)
input.config(highlightbackground = "white", highlightcolor= "white")

one=Button(main, text="1", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(1), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
one.grid(row=3, column=1, padx=5, pady=5)
two=Button(main, text="2", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(2), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
two.grid(row=3, column=2, padx=5, pady=5)
three=Button(main, text="3", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(3), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
three.grid(row=3, column=3, padx=5, pady=5)
four=Button(main, text="4", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(4), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
four.grid(row=2, column=1, padx=5, pady=5)
five=Button(main, text="5", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(5), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
five.grid(row=2, column=2, padx=5, pady=5)
six=Button(main, text="6", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(6), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
six.grid(row=2, column=3, padx=5, pady=5)
seven=Button(main, text="7", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(7), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
seven.grid(row=1, column=1, padx=5, pady=5)
eight=Button(main, text="8", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(8), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
eight.grid(row=1, column=2, padx=5, pady=5)
nine=Button(main, text="9", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(9), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
nine.grid(row=1, column=3, padx=5, pady=5)
zero=Button(main, text="0", padx=20, pady=20, font=("arial 10 bold"), command=lambda: numclick(0), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
zero.grid(row=4, column=1, padx=5, pady=5)

decimal=Button(main, text=".", padx=22, pady=20, font=("arial 10 bold"), command=lambda:deciclick("."), bg="#b0b0b6", cursor="hand2", activebackground="#9E9FA5")
decimal.grid(row=4, column=2, padx=5, pady=5)
sqr=Button(main, text="\u221A", padx=20, pady=20, font=("arial 10 bold"), command=sqrclick, bg="#FF9500", cursor="hand2", activebackground="#9E9FA5")
sqr.grid(row=1, column=4, padx=5, pady=5)
clr=Button(main, text="C", padx=20, pady=20, font=("arial 10 bold"), command=clrclick, bg="#FF9500", cursor="hand2", activebackground="red")
clr.grid(row=1, column=5, padx=5, pady=5)
add=Button(main, text="+", padx=55, pady=20, font=("arial 10 bold"), command=addclick, bg="#FF9500", cursor="plus", activebackground="#9E9FA5")
add.grid(row=4, column=3, padx=5, pady=5, columnspan=2)
sub=Button(main, text="-", padx=20, pady=20, font=("arial 10 bold"), command=subclick, bg="#FF9500", cursor="hand2", activebackground="#9E9FA5")
sub.grid(row=3, column=4, padx=5, pady=5)
mul=Button(main, text="X", padx=20, pady=20, font=("arial 10 bold"), command=mulclick, bg="#FF9500", cursor="hand2", activebackground="#9E9FA5")
mul.grid(row=2, column=5, padx=5, pady=5)
div=Button(main, text="\u00F7", padx=20, pady=20, font=("arial 10 bold"), command=divclick, bg="#FF9500", cursor="hand2", activebackground="#9E9FA5")
div.grid(row=2, column=4, padx=5, pady=5)
eql=Button(main, text="=", padx=20, pady=59, font=("arial 10 bold"), command=eqlclick, bg="#FF9500", cursor="hand2", activebackground="#9E9FA5")
eql.grid(row=3, column=5, padx=5, pady=5, rowspan=2)

main.mainloop()