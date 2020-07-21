import random
from modules import engine, Password
from sqlalchemy.orm import sessionmaker
from tkinter import *
import string

Session = sessionmaker(bind=engine)
session = Session()

main_screen = Tk()
main_screen.title("Password generator")
main_screen.geometry("550x600")



name = Label(main_screen, text="Password generator", bg="grey", width="400", height="5", font=("Calibri", 17)).pack()
namelabel = Label(main_screen, text="Name").pack()
nameentry = Entry(main_screen)
nameentry.pack()
button2 = Button(main_screen, text="Copy")
Label(text="Password length: ", font=("Calibri", 18)).pack()
var = IntVar()
scale = Scale(main_screen, variable=var, from_=4, to_=22, font=("Calibri", 18), orient=HORIZONTAL,
              tickinterval=18).pack()

title = StringVar()
label = Label(main_screen, textvariable=title, anchor=N, pady=10).pack()
title.set("Password strength:")

psswrd = StringVar()




def select():
    selection = choice.get()


choice = IntVar()
r1 = Radiobutton(main_screen, text="BASIC", variable=choice, value=1, command=select).pack(anchor=CENTER)
r2 = Radiobutton(main_screen, text="MEDIUM", variable=choice, value=2, command=select).pack(anchor=CENTER)
r3 = Radiobutton(main_screen, text="EXTRA", variable=choice, value=3, command=select).pack(anchor=CENTER)

lsum = Label(main_screen, text="")
lsum.pack(side=BOTTOM)


def passgen(event):
    result = ""

    if choice.get() == 1:
        result = "".join(random.sample(lower + num, var.get()))
    elif choice.get() == 2:
        result = "".join(random.sample(lower + upper + num, var.get()))
    elif choice.get() == 3:
        result = "".join(random.sample(lower + upper + num + sym, var.get()))

    lsum.config(text=result)
    password = Password(nameentry.get(), result)
    psswrd.set(result)
    session.add(password)
    session.commit()
    box.delete(0,END)
    box.insert(END, *session.query(Password).all())


def copy_password(event):
    main_screen.clipboard_clear()
    main_screen.clipboard_append(session.query(Password).all()[box.curselection()[0]].pssw)
    main_screen.update()

button2.bind("<Button-1>", copy_password)



num = string.digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
sym = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""

button = Button(main_screen, text="Generate Password", relief=RIDGE, bd=5, height=2, pady=4)
button.pack()
button.bind("<Button-1>", passgen)




box = Listbox(main_screen, selectmode=SINGLE)
box.insert(END, *session.query(Password).all())
box.pack()

button2.pack()


main_screen.mainloop()
#
#
#
#
#
#
#
#
#
# import random
# from sqlalchemy.orm import sessionmaker
# from tkinter import *
# import string
# from cgitb import text
# from logging import root
# from modules import Password, engine
#
#
#
#
#
# main_screen = Tk()
# main_screen.title("Password generator")
# main_screen.geometry("550x600")
#
# name = Label(main_screen, text="Password generator", bg="grey", width="400", height="5", font=("Calibri", 17)).pack()
# Label(text="Password length: ", font=("Calibri", 18)).pack()
# var = IntVar()
# scale = Scale(main_screen, variable=var, from_=4, to_=22, font=("Calibri", 18), orient=HORIZONTAL,
#               tickinterval=18).pack()
#
# scrollbar = Scrollbar(main_screen)
# scrollbar.config(command=box.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# btn= Button(main_screen, text="Generate password", command=gen)
# btn.pack
# box = Listbox(main_screen, selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
# box.insert(*END)
# box.pack()
# #
# #
# def generate_password():
#     password=[]
#     for x in range(9):
#         alpha=random.choice(string.ascii_letters)
#         symbol=random.choice(string.punctuation)
#         numbers=random.choice(string.digits)
#         password.append(alpha)
#         password.append(symbol)
#         password.append(numbers)
#
#     y="".join(str(x)for x in password)
#     lbl.config(text=y)
# #
# btn=Button(root,text="generate password",command=generate_password)
# btn.grid(row=2,column=2)
# lbl=Label(root,font=("times",15,"bold"))
# lbl.grid(row=4,column=2)
# root.mainloop()
# #
# #
# #
# # #
# # # #
# title = StringVar()
# label = Label(main_screen, textvariable=title, anchor=N, pady=10).pack()
# title.set("Password strength:")
#
# #
# # def select():
# #     selection = choice.get()
# #
# # choice = IntVar()
# # r1 = Radiobutton(main_screen, text="BASIC", variable=choice, value=1, command=select).pack(anchor=CENTER)
# # r2 = Radiobutton(main_screen, text="MEDIUM", variable=choice, value=2, command=select).pack(anchor=CENTER)
# # r3 = Radiobutton(main_screen, text="EXTRA", variable=choice, value=3, command=select).pack(anchor=CENTER)
# #
# #
# # lsum = Label(main_screen, text="")
# # lsum.pack(side=BOTTOM)
# #
# # def callback():
# #  lsum.config(text=passgen())
# #
# #
# #
# # num = string.ascii_uppercase + string.digits
# # low = string.ascii_lowercase
# # sym = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
# # everything = num + low + sym
# #
# # button = Button(main_screen, text="Generate Password", relief=RIDGE, bd=5, height=2, command=callback, pady=4)
# # button.pack()
# # password = str(callback)
# #
# #
# # #
# # def passgen():
# #     if choice.get() == 1:
# #         return "".join(random.sample(num, val.get()))
# #     elif choice.get() == 2:
# #         return "".join(random.sample(low, val.get()))
# #     elif choice.get() == 3:
# #         return "".join(random.sample(everything, val.get()))
# #
# # box = Listbox(main_screen)
# # box.pack(pady=50)
#
# main_screen.mainloop()