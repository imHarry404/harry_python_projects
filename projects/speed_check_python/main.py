from tkinter import *
from tkinter import messagebox
import pyspeedtest

def logic():
    st-pyspeedtest.SpeedTest('www.google.com')
    a=(str(st.download())+" bytes per second")
    messagebox.showinfo('your download speed is ',a)

top=Tk()
top.title("speed test by harry")
top.geometry('100x100')
filename = PhotoImage(file="C:\\Users\\hario\\Desktop\\ok.png")

background_label=Label(top,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

b=Button("Click to see the Internet speed: ",font=('San serif',20),height=1,width=30,command=logic).pack()
top.mainloop()
