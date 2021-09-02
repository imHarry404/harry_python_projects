# in this project we ask the review and rating from the user and show them a message
import tkinter.messagebox
from tkinter import *

root = Tk()
root.title("Harry Chai")
root.geometry('450x550')
root.maxsize(600, 600)
root.minsize(550, 450)

# creating scale to take user input
heading = "Welcome to Python Chai Corner Wala"
Label(root, text=f"{heading}", font='lucika 20 bold', bg='red', fg='white', padx=20, pady=10).grid()
order = "Select your desired Flavour of C#@!_Harry"
ads = Label(root, text=f'{order}', font='lucika 15 bold').grid()


# yesb hmara menu ka content hoga
# chai(10), chai_paoda(15),
# (30),special_chai(25),chai_desi(15),chai_malai(29),coffee(20)# creating the order content
def ordernow():
    """
    if Chai_var.get():
        print("ok true")
    else:
        print('false')

    """
    # reading the checkboxes are saving the price like bill and notify the user that order placed and print bill now
    """
    with open('chai_ke_oder_ki_details.txt', 'a') as chai_ka_order:
        if Chai_var.get() or Chai_desi_var.get() or Chai_pakoda_var.get() or Kulhar_cahi_var.get() or 
        Chai_malai_var.get() or Coffee_var.get():
            chai_ka_order.write(f'Your Order Details are\n
                                Chai          -> Rs {Chai_var_rate}\n'
                                f'Chai_desi     -> Rs {Chai_desi_rate}\n'
                                f'Chai_pakoda   -> Rs {Chai_pakoda_rate}\n'
                                f'Kulhar_cahi   -> Rs {Kulhar_cahi_rate}\n'
                                f'Chai_malai    -> Rs {Chai_malai_rate}\n'
                                f'Coffee        -> Rs {Coffee_rate}\n\n')
    chai_ka_order.close() """
    total_price = 0
    with open('chai_ke_oder_ki_details.txt', 'w') as chai_ka_order:
        chai_ka_order.write('Your Order Details are\n')
        if Chai_var.get():
            chai_ka_order.write(f"Chai-> Rs {Chai_var_rate}\n")
            total_price += Chai_var_rate

        if Chai_desi_var.get():
            chai_ka_order.write(f"Chai_desi -> Rs {Chai_desi_rate}\n")
            total_price += Chai_desi_rate

        if Chai_pakoda_var.get():
            chai_ka_order.write(f"Chai_pakoda -> Rs {Chai_pakoda_rate}\n")
            total_price += Chai_pakoda_rate

        if Kulhar_cahi_var.get():
            chai_ka_order.write(f"Kulhar_cahi -> Rs {Kulhar_cahi_rate}\n")
            total_price += Kulhar_cahi_rate

        if Chai_malai_var.get():
            chai_ka_order.write(f"Chai_malai -> Rs {Chai_malai_rate}\n")
            total_price += Chai_malai_rate

        if Coffee_var.get():
            chai_ka_order.write(f"Coffee_var -> Rs {Coffee_rate}\n")
            total_price += Coffee_rate
        if Special_chai_var.get():
            chai_ka_order.write(f"Coffee_var -> Rs {Special_chai_rate}\n")
            total_price += Special_chai_rate

        chai_ka_order.write(f'Total Bill->{total_price}\n')
    tkinter.messagebox.showinfo("done", "Order placed successfully")
    print_bill()


def print_bill():
    # reading the file and printing the bill
    with open('chai_ke_oder_ki_details.txt', 'r') as bill:
        # data = bill.read()
        tkinter.messagebox.showinfo('thanks', f'{bill.read()}')

    tkinter.messagebox.showinfo("Thanks", "Order again, thanks a lot")
    # asking for review the app
    if tkinter.messagebox.askquestion('Review', "Do you like this app and write how can we improve better") == 'yes':
        take_review()


# storing the review in the main file
def submit_rev():
    with open('chai_ke_oder_ki_details.txt', 'a') as rev:
        rev.write(f'\nYour valuable feedback is \n{a.get()}'
                  f'\nYour name is {name_var.get()}\n'
                  f'Your phone no is {phone_var.get()}')
    print_data()


def print_data():
    with open('chai_ke_oder_ki_details.txt', 'r') as data:
        print(data.read())


# # asking the name
# def ask_name():
#     with open('chai_ke_oder_ki_details.txt', 'a+') as name_phone:
#         name_phone.write(f'\nYour name is \n{name_var.get()}'
#                          f'your phone is {phone_var.get()}\n')


a = StringVar()  # this is to store the review
name_var = StringVar()
phone_var = StringVar()


def take_review():
    Label(root, text="Enter your Name").grid()
    Entry(root, textvariable=name_var).grid()
    Label(root, text="Enter your Phone").grid()
    Entry(root, textvariable=phone_var).grid()
    Label(root, text="Write your review here").grid()
    Entry(root, textvariable=a).grid()
    Label(root, text="Rate us out of 5").grid()
    my_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, tickinterval=float(.5))
    my_scale.grid()
    Button(root, text="Submit Review", command=submit_rev, bg='black', fg='white').grid()


# rate for bill
Chai_var_rate = 5
Chai_pakoda_rate = 20
Kulhar_cahi_rate = 30
Special_chai_rate = 21
Chai_desi_rate = 21
Chai_malai_rate = 29
Coffee_rate = 30

# variables
Chai_var = IntVar()
Chai_pakoda_var = IntVar()
Kulhar_cahi_var = IntVar()
Special_chai_var = IntVar()
Chai_desi_var = IntVar()
Chai_malai_var = IntVar()
Coffee_var = IntVar()

# C1 = Checkbutton(root, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)

Chai = Checkbutton(text=f"Chai Rs {Chai_var_rate}", variable=Chai_var, onvalue=1, offvalue=0).grid(row=5, column=0)

Chai_pakoda = Checkbutton(text=f"Chai_pakoda Rs {Chai_pakoda_rate}", variable=Chai_pakoda_var, onvalue=1,
                          offvalue=0).grid(row=6,
                                           column=0)
Kulhar_cahi = Checkbutton(text=f"Kulhar_cahi Rs {Kulhar_cahi_rate}", variable=Kulhar_cahi_var, onvalue=1,
                          offvalue=0).grid(row=7,
                                           column=0)
Special_chai = Checkbutton(text=f"Special_chai Rs {Special_chai_rate}", variable=Special_chai_var, onvalue=1,
                           offvalue=0).grid(
    row=8,
    column=0)
Chai_desi = Checkbutton(text=f"Chai_desi Rs {Chai_desi_rate}", variable=Chai_desi_var, onvalue=1, offvalue=0).grid(
    row=9,
    column=0)

Chai_malai = Checkbutton(text=f"Chai_malai Rs {Chai_malai_rate}", variable=Chai_malai_var, onvalue=1, offvalue=0).grid(
    row=10,
    column=0)

Coffee = Checkbutton(text=f"Coffee Rs {Coffee_rate}", variable=Coffee_var, onvalue=1, offvalue=0).grid(row=11, column=0)

Button(text="Order Now", command=ordernow).grid()

# tick krawayenge order pe and file me usko write krenge and then usko price show krenge and then feedback lenge and
# usko v save krenge

# last me ek Order_now ka button hoga and wo data ko ek file me save kr dega and then usi file me se read krke rate show
# krega and then review ek new file me save krega

root.mainloop()
