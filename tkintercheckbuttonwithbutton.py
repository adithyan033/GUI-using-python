from tkinter import *

root = Tk()

var = IntVar()

def show():
    print(var.get())

cb = Checkbutton(root, text="Enable feature", variable=var)
cb.pack()

btn = Button(root, text="Check Value", command=show)
btn.pack()

root.mainloop()