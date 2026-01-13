from tkinter import *

# create main window
root = Tk()
root.title("Arithmetic Operations")
root.geometry("300x250")

# labels
Label(root, text="Enter First Number").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Enter Second Number").pack()
e2 = Entry(root)
e2.pack()

# label to show result
result_label = Label(root, text="Result: ")
result_label.pack(pady=10)

# functions for operations
def add():
    a = int(e1.get())
    b = int(e2.get())
    result_label.config(text="Result: " + str(a + b))

def sub():
    a = int(e1.get())
    b = int(e2.get())
    result_label.config(text="Result: " + str(a - b))

def mul():
    a = int(e1.get())
    b = int(e2.get())
    result_label.config(text="Result: " + str(a * b))

def div():
    a = int(e1.get())
    b = int(e2.get())
    result_label.config(text="Result: " + str(a / b))

# buttons
Button(root, text="Add", command=add).pack()
Button(root, text="Sub", command=sub).pack()
Button(root, text="Mul", command=mul).pack()
Button(root, text="Div", command=div).pack()

# run the GUI
root.mainloop()
