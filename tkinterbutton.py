from tkinter import *

root = Tk()
frame=Frame(root)
frame.pack()

def show():
    print("fucku")

btn = Button(frame, text="Click Me",command=show)
btn.pack()


root.mainloop()
