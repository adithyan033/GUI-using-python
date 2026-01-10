from tkinter import *

root = Tk()

# Control variable
choice = IntVar()

# Radio buttons
r1 = Radiobutton(root, text="Male", variable=choice, value=1)
r2 = Radiobutton(root, text="Female", variable=choice, value=2)
r3 = Radiobutton(root, text="Other", variable=choice, value=3)

r1.pack()
r2.pack()
r3.pack()

root.mainloop()
