from tkinter import *
from tkinter.ttk import *
import random
#import pyperclip

def random_pass():
    password_output.delete(0, END)
    length=len.get()
    weak="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    medium="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    strong="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    gen_password=""
    if sec.get()==1:
        for i in range(0, length):
            gen_password = gen_password + random.choice(weak)
    elif sec.get()==2:
        for i in range(0, length):
            gen_password = gen_password + random.choice(medium)
    elif sec.get()==3:
        for i in range(0, length):
            gen_password = gen_password + random.choice(strong)
    else:
        print("Enter the type of security required!")
    
    return gen_password

def generate():
    password1=random_pass()
    password_output.insert(0, password1)

def copy():
    password2=password_output.get()
    pyperclip.copy(password2)

main=Tk()
main.title("Password Generator")
main.geometry("430x200")
main.resizable(0, 0)

sec=IntVar()
len=IntVar()

t1=Label(main, text="Enter the length of the password :") 
t1.grid(row=0, column=0, padx=0)
t2=Label(main, text="    Select the security of your password :")
t2.grid(row=1, column=0, padx=0)
t3=Label(main, text="The Generated Password is :", font="Georgia 15 italic")
t3.grid(row=5, column=0, pady=0, columnspan=4)

length=Spinbox(main, from_=4, to_=32, textvariable=len, width=5)
length.grid(row=0, column=1, padx=0, pady=20)
security1=Radiobutton(main, text="Weak", variable=sec, value=1)
security1.grid(row=1, column=1, padx=5, sticky="E")
security2=Radiobutton(main, text="Medium", variable=sec, value=2)
security2.grid(row=1, column=2, padx=5, sticky="W")
security3=Radiobutton(main, text="Strong", variable=sec, value=3)
security3.grid(row=1, column=3, padx=5, sticky="W")
enter=Button(main, text="Generate", command=generate, width=9)
enter.grid(row=2, column=1, pady=10)
copy1=Button(main, text="Copy", command=copy, width=8)
copy1.grid(row=6, column=3)
password_output=Entry(main, width=40, font="arial 8 bold", foreground="red")
password_output.grid(row=6, column=0, columnspan=4, pady=5)

main.mainloop()