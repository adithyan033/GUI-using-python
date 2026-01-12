from tkinter import *

root = Tk()

msg = Message(root,
              text=" say my name!",
              width=100,
              bg="yellow",
              fg="red",
              font=("Arial", 12))
msg.pack(padx=100,pady=100)

root.mainloop()
