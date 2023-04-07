#import libraries
import random
import tkinter.messagebox
from tkinter import *
import string
import tkinter as tk
import pyperclip as pc

#create UI
window = Tk()
canvas1 = tk.Canvas(window, width=500, height=300, relief='flat')
canvas1.pack()

window.title('Password Generator')

label1 = tk.Label (window, font=('bold', 10), text='PASSWORD GENERATOR')
canvas1.create_window(250,25, window=label1)

label2 = tk.Label (window, text='Enter Password Length (8 to 32 Characters)', font=('normal', 10))
canvas1.create_window(250,100, window=label2)

entry1 = tk.Entry(window)
canvas1.create_window(250, 140, window=entry1)

#define password
def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@_$%'
    password = ''.join(random.sample(valid_char, leng))
    pc.copy(password)
    Label (window, text="Password Automatically Copied To Clipboard", fg='green', font=('bold', 20)).pack()

#determine password
def get_len():
    password_len = int(entry1.get())
    if (32 >= password_len >= 8):
        password_generate(password_len)
    else:
        Label(window, text='Error: Please try again.', font=('bold', 20), fg='red').place(x=120, y=200)

#generate Generate button
Button (window, text='Generate Password', font=('normal', 10), bg='yellow', command=get_len).pack()

window.mainloop()