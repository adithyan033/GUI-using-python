from tkinter import *

def change_text():
    label.config(text="Button Clicked")

root = Tk()

label = Label(root, text="Click the button",fg="blue")
label.pack()

btn = Button(root, text="Click Me", bg="red",command=change_text)
btn.pack()

root.mainloop()
