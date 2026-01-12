from tkinter import *

root = Tk()
root.title("Spinbox Example")
root.geometry("250x150")

Label(root, text="Select Age").pack(pady=5)

spin = Spinbox(root, from_=1, to=100, width=10)
spin.pack()

def show():
    print("Selected Age:", spin.get())

Button(root, text="Show", command=show).pack(pady=10)

root.mainloop()
