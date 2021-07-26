# importing the required library
from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk() #creating the tkinter object
root.title('Harry_Clock') #setting title 

def time():
    string=strftime('%H:%M:%S %p') #time format
    label.config(text=string)
    label.after(1000,time) 
 
label=Label(root,font=('ds-digital',80),background='black',foreground='white') #binding the labels
label.pack(anchor='center') #packing the label in the center
time()
mainloop() 

# download the ds-digital font from here: https://www.dafont.com/ds-digital.font
