# importing the required modules
from tkinter import *
from string import ascii_uppercase,ascii_lowercase,digits,punctuation
from random import sample

# creating the mainloop
root = Tk()
root.geometry("400x280")
root.title("Password Generator-- Harry")

# title for the app
title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Choose Your Password Category:")



def selection():
    selection = choice.get()

# for opetions
choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

# for length of the password
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

#bounding the  password length as minimum is 8 and maximum is 24
val = IntVar()
spinlenght = Spinbox(root, from_=8, to_=24, textvariable=val, width=13).pack()


# passprint
def callback():
    lsum.config(text=passgen())


# clickable button
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3,activebackground = "pink",activeforeground = "blue")
passgenButton.pack()
password = str(callback)

# password result message
lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# password categogy using string module 
poor= ascii_uppercase + ascii_lowercase 
average= ascii_uppercase + ascii_lowercase + digits
strong = poor+ average + punctuation


# main function to return the password as per user selection
def passgen():
    if choice.get() == 1:
        return "".join(sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(sample(strong, val.get()))


root.mainloop()