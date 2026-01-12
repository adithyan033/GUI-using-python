from tkinter import *

root = Tk()

text = Text(root, width=30, height=10)
text.pack(side=RIGHT)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)

root.mainloop()
