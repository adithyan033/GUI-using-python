from tkinter import *

root = Tk()

frame = Frame(root, bg="blue", bd=5)
frame.pack(padx=100, pady=100)

Label(frame, text="Username").pack()
Entry(frame).pack()
root.mainloop()
