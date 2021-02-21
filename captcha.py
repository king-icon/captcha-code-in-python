import random 
from tkinter import *
from tkinter import messagebox
text = "abcdefghijklmnopqrstuvwxyz1234567890"
window = Tk()
window.title("captcha app")
window.geometry("300x100")
captcha = StringVar()
user_input = StringVar()

def set_captcha():
    s = random.choices(text,k = 6)
    captcha.set(''.join(s))

def check():
    if captcha.get() == user_input.get():
        messagebox.showinfo("success","correct")
    else:
        messagebox.showerror("error","incorrect")
    set_captcha()

Label(window,textvariable = captcha,
    font = "arial 16 bold").pack()
Entry(window,textvariable = user_input,
    font = "arial 10 bold").pack(ipady = 5)
Button(window,command = check,text = "check",
    font = "arial 10").pack()
set_captcha()
window.mainloop()


