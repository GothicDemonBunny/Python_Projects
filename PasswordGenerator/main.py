#import libraries
from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter

#create UI
window = Tk()
window.title('Password Generator')
window.geometry('500x500')

Label (window, font=('bold', 10), text='PASSWORD GENERATOR').pack()

#define functions
def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@_$%'
    password=''.join(random.sample(valid_char, leng))
    l = Label(window, text= password, font=('bold', 20))
    l.place(x=90, y=50)

#determine password
def get_len():
    if (32 >= password_len >= 8):
        password_generate(password_len)
    else:
        print("Invalid input. Ending application.")
        exit()


#password length variable
password_len = int (input("Enter password length between 8 and 32 characters: "))

#generate Generate button
Button (window, text='Generate Password', font=('normal', 10), bg='yellow', command=get_len).place(x=200,y=100)

window.mainloop()